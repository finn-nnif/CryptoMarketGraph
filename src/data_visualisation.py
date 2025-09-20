from src.utility.util_graph import move_legend_outside
from config.config import COLOUR_PALETTE
from matplotlib import cm
import matplotlib.pyplot as plt
import seaborn as sns



def plot_histogram(df, column, bins=30, add_legend=False):
    sns.set_palette(COLOUR_PALETTE)
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=bins, kde=True)
    if not add_legend and plt.gca().get_legend() is not None:
        plt.gca().get_legend().remove()
    plt.title(f'Histogram of {column}')
    plt.show()



def plot_scatter(df, x_col, y_col, category_col, add_legend=True):
    fig, ax = plt.subplots(figsize=(10, 6))

    df[category_col] = df[category_col].astype(str)
    n_categories = df[category_col].nunique()

    # generate colors from the colormap
    cmap = cm.get_cmap(COLOUR_PALETTE, n_categories)
    palette = [cmap(i) for i in range(n_categories)]

    sns.scatterplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=category_col,
        palette=palette,
        ax=ax
    )

    if not add_legend and ax.get_legend() is not None:
        ax.get_legend().remove()
    else:
        move_legend_outside(ax)

    return fig, ax



def plot_line(df, x_col, y_col, show_ci=True, add_legend=False):
    sns.set_palette(COLOUR_PALETTE)
    fig, ax = plt.subplots(figsize=(10, 6))
    errorbar = 'ci' if show_ci else None
    sns.lineplot(data=df, x=x_col, y=y_col, ax=ax, errorbar=errorbar)
    if not add_legend and ax.get_legend() is not None:
        ax.get_legend().remove()
    return fig, ax


def plot_multi_line(df, x_col, y_cols, show_ci=True, add_legend=True):
    sns.set_palette(COLOUR_PALETTE, len(y_cols))
    fig, ax = plt.subplots(figsize=(12, 6))
    errorbar = 'ci' if show_ci else None

    for col in y_cols:
        sns.lineplot(
            data=df,
            x=x_col,
            y=col,
            ax=ax,
            label=col.replace('_', ' ').title(),
            errorbar=errorbar
        )

    if not add_legend and ax.get_legend() is not None:
        ax.get_legend().remove()

    return fig, ax