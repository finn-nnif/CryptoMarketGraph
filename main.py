from src import *
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import yaml

with open("config/presets.yaml", "r") as f:
    cfg = yaml.safe_load(f)

graph_presets = cfg["graph_presets"]

def load_preset(preset_name: str):
    cfg = graph_presets[preset_name]

    # LOAD + CLEAN

    df = load_csv_all(cfg["file"])
    df = clean_data(df, drop_duplicates=False)

    try:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    except Exception as e:
        print("Timestamp conversion failed:", e)


    if "values_col" in cfg and cfg["values_col"] in df.columns:
        if df[cfg["values_col"]].dtype == "object":
            df[cfg["values_col"]] = (
                df[cfg["values_col"]]
                .astype(str)
                .str.replace(r"[$,%MBT+]", "", regex=True)
                .astype(float)
            )

    if cfg["plot_func"] == "scatter":
        for col in [cfg["x_col"], cfg["y_col"]]:
            if col in df.columns and df[col].dtype == "object":
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(r"[$,%MBT+]", "", regex=True)
                    .astype(float)
                )
        df = df.dropna(subset=[cfg["x_col"], cfg["y_col"]])

    # PIVOT if needed

    df_pivot = None
    y_cols = None
    if cfg["plot_func"] == "multi_line":
        df_pivot = pivot_data(
            df,
            index_col=cfg["index_col"],
            columns_col=cfg["columns_col"],
            values_col=cfg["values_col"]
        )
        y_cols = [c for c in df_pivot.columns if c not in cfg.get("exclude_coins", [])]

    # PLOT

    if cfg["plot_func"] == "multi_line":
        fig, ax = plot_multi_line(
            df_pivot.reset_index(),
            x_col=cfg["index_col"],
            y_cols=y_cols,
            show_ci=False,
            add_legend=False
        )
        df_reset = df_pivot.reset_index()
        style_line_annotation(ax, df_reset, y_cols,
                              x_col=cfg["index_col"],
                              offset_days=6,
                              color=(1,1,1),
                              alpha=0.7)

        # Y-LIM

        ymin, ymax = 0, df_pivot[y_cols].max().max()
        ymax_rounded = round_up_to_nearest(ymax)
        offset = 0.02 * ymax_rounded
        ax.set_ylim(ymin, ymax + offset)

    elif cfg["plot_func"] == "scatter":
        fig, ax = plot_scatter(
            df,
            x_col=cfg["x_col"],
            y_col=cfg["y_col"],
            category_col=cfg["category_col"],
            add_legend=False
        )
        design_points(
            ax,
            point_size=50,
            facecolor=None,         # None keeps the Seaborn Palette
            edgecolor="none",
            alpha=0.8
        )
    else:
        raise NotImplementedError(f"plot_func '{cfg['plot_func']}' not implemented.")

    # STYLE PLOT

    style_plot(ax,
        grid=True,
        grid_color=(1/3, 1/3, 1/3),
        grid_linestyle="--",
        grid_linewidth=0.5,
        title=cfg.get("title", ""),
        xlabel=cfg.get("xlabel", ""),
        ylabel=cfg.get("ylabel", ""),
        xtick_rotation=45,
        legend=False,
        fig_facecolor=(4/255,4/255,4/255),
        ax_facecolor=(4/255,4/255,4/255),
        title_color=(1,1,1),
        label_color=(1,1,1),
        tick_color=(1,1,1),
        spine_color=(1,1,1)
    )

    plt.show()

###

if __name__ == "__main__":
    load_preset("change_scatter")