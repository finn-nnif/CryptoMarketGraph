
from config.config import COLOUR_PALETTE
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column, bins=30):
    sns.set_palette(COLOUR_PALETTE)
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()


def plot_scatter(df, x_col, y_col):
    sns.set_palette(COLOUR_PALETTE)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    return fig, ax


def plot_line(df, x_col, y_col, show_ci=True):
    sns.set_palette(COLOUR_PALETTE)
    fig, ax = plt.subplots(figsize=(10, 6))
    errorbar = 'ci' if show_ci else None
    sns.lineplot(data=df, x=x_col, y=y_col, ax=ax, errorbar=errorbar)
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