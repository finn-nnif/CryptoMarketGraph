from src import *
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

if __name__ == "__main__":

    # LOAD
    df = load_csv_all('data/raw/cryptocurrency.csv')

    # CLEAN
    df_clean = clean_data(df, drop_duplicates=False)
    df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])

    df_clean = remove_char(df_clean, 'price_usd', '$')
    df_clean = remove_char(df_clean, 'price_usd', ',')
    df_clean['price_usd'] = df_clean['price_usd'].astype(float)

    # PIVOT
    df_pivot = pivot_data(df_clean, index_col='timestamp', columns_col='symbol', values_col='price_usd')

    all_coins = [col for col in df_pivot.columns if not df_pivot[col].isna().all()]
    exclude_coins = ['BTC', 'ETH']

    y_cols = []
    for coin in all_coins:
        if coin not in exclude_coins:
            y_cols.append(coin)

    # PLOT
    fig, ax = plot_multi_line(df_pivot.reset_index(), x_col='timestamp', y_cols=y_cols, show_ci=False, add_legend=False)


    design_lines(
        ax,
        colors=None,
        linewidths=[1] * len(y_cols),
        linestyles=['-'] * len(y_cols),
        alphas=[0.8] * len(y_cols)
    )

    df_reset = df_pivot.reset_index()
    style_line_annotation(ax, df_reset, y_cols, x_col='timestamp', offset_days=6, color=(1, 1,1), alpha=0.7)


    style_plot(
        ax,
        grid=True,
        grid_color=(1/3, 1/3, 1/3),
        grid_linestyle='--',
        grid_linewidth=0.5,
        title="Crypto Prices Over Time",
        xlabel="Timestamp",
        ylabel="Price (USD)",
        xtick_rotation=45,
        legend=False,
        fig_facecolor=  (4 / 255, 4 / 255, 4 / 255),     # '#111111'
        ax_facecolor=   (4 / 255, 4 / 255, 4 / 255),      # '#222222'
        title_color=    (1, 1, 1),                      # white
        label_color=    (1, 1, 1),                      # white
        tick_color=     (1, 1, 1),                       # white
        spine_color=    (1, 1, 1)                       # white
    )


    ymin = 0
    ymax = df_pivot[y_cols].max().max()
    ymax_rounded = round_up_to_nearest(ymax)
    ax.set_ylim(ymin, ymax_rounded)

    plt.show()
