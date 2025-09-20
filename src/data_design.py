from datetime import timedelta
import matplotlib.colors as mcolors

def style_plot(ax, grid=True, tight_layout=True, **kwargs):
    """
    Universal plot styling function.
    """
    # Background colors
    if "fig_facecolor" in kwargs:
        ax.figure.patch.set_facecolor(kwargs["fig_facecolor"])
    if "ax_facecolor" in kwargs:
        ax.set_facecolor(kwargs["ax_facecolor"])

    # Title and labels
    if "title" in kwargs:
        ax.set_title(kwargs["title"], fontsize=kwargs.get("title_fontsize", 14), color=kwargs.get("title_color", 'black'))

    if "xlabel" in kwargs:
        ax.set_xlabel(kwargs["xlabel"], fontsize=kwargs.get("label_fontsize", 12), color=kwargs.get("label_color", 'black'))

    if "ylabel" in kwargs:
        ax.set_ylabel(kwargs["ylabel"], fontsize=kwargs.get("label_fontsize", 12), color=kwargs.get("label_color", 'black'))

    # Tick styling
    ax.tick_params(axis='x', rotation=kwargs.get("xtick_rotation", 0), colors=kwargs.get("tick_color", 'black'))
    ax.tick_params(axis='y', rotation=kwargs.get("ytick_rotation", 0), colors=kwargs.get("tick_color", 'black'))

    # Spines (axes borders)
    spine_color = kwargs.get("spine_color", 'black')
    for spine in ax.spines.values():
        spine.set_color(spine_color)

    # Axis limits
    if "xlim" in kwargs:
        ax.set_xlim(kwargs["xlim"])
    if "ylim" in kwargs:
        ax.set_ylim(kwargs["ylim"])

    # Legend
    if kwargs.get("legend", False):
        loc = kwargs.get("legend_loc", "best")
        bbox = kwargs.get("legend_bbox_to_anchor", None)
        legend = ax.legend(loc=loc, bbox_to_anchor=bbox) if bbox else ax.legend(loc=loc)
        if "legend_text_color" in kwargs:
            for text in legend.get_texts():
                text.set_color(kwargs["legend_text_color"])

    # Grid
    if grid:
        grid_color = kwargs.get("grid_color", None)
        grid_linestyle = kwargs.get("grid_linestyle", None)
        grid_linewidth = kwargs.get("grid_linewidth", None)
        ax.grid(True,
                color=grid_color,
                linestyle=grid_linestyle,
                linewidth=grid_linewidth)
    else:
        ax.grid(False)

    # Tight layout
    if tight_layout:
        ax.figure.tight_layout()

    return ax




def style_title(t):
    return t.replace("_", " ").title()



from datetime import timedelta

def style_line_annotation(ax, df, y_cols, x_col='timestamp', offset_days=5, fontsize=9, color='white', alpha=1.0):
    offset = timedelta(days=offset_days)
    x = df[x_col]

    # Combine color and alpha properly
    rgba_color = mcolors.to_rgba(color, alpha)

    for col in y_cols:
        y = df[col]
        last_valid_idx = y.last_valid_index()
        if last_valid_idx is None:
            continue
        x_last = x.loc[last_valid_idx]
        y_last = y.loc[last_valid_idx]

        ax.text(
            x_last + offset, y_last, col,
            fontsize=fontsize,
            color=rgba_color,
            verticalalignment='center',
            horizontalalignment='right'
        )



def design_points(ax, point_size=None, facecolor=None, edgecolor=None, alpha=None):
    """
    Parameters:
        ax (matplotlib.axes.Axes): The axes containing the plot.
        point_size (float): New size for scatter points (points^2).
        facecolor (tuple or str): Color for the points' face.
        edgecolor (tuple or str): Color for the points' edge.
        alpha (float): Transparency level for the points.
    """
    for collection in ax.collections:
        if point_size is not None:
            collection.set_sizes([point_size])
        if facecolor is not None:
            collection.set_facecolor(facecolor)
        if edgecolor is not None:
            collection.set_edgecolor(edgecolor)
        if alpha is not None:
            collection.set_alpha(alpha)



def expand_limits(ax, df=None, y_cols=None, padding_ratio=0.05, min_padding=1):
    """
    Expand axis limits with padding, based on data if given,
    but never less than min_padding units.

    Parameters:
        ax (matplotlib.axes.Axes): The axes to expand limits on.
        df (pd.DataFrame, optional): DataFrame with the data plotted.
        y_cols (list of str, optional): Columns in df to consider for y-limits.
        padding_ratio (float): Fractional padding relative to data range.
        min_padding (float): Minimum padding to add (in data units).
    """
    
    if df is not None and y_cols is not None:
        y_min = df[y_cols].min().min()
        y_max = df[y_cols].max().max()
        ylim = (y_min, y_max)
    else:
        ylim = ax.get_ylim()
    
    xlim = ax.get_xlim()

    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]

    if x_range == 0:
        x_range = 1
    if y_range == 0:
        y_range = 1

    x_pad = max(x_range * padding_ratio, min_padding)
    y_pad = max(y_range * padding_ratio, min_padding)

    ax.set_xlim(xlim[0] - x_pad, xlim[1] + x_pad)
    ax.set_ylim(ylim[0] - y_pad, ylim[1] + y_pad)