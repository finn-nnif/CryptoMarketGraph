
def move_legend_outside(ax, border_pad=0.01):
    """
    Moves the legend outside the axes on the right, vertically centered,
    only if a legend exists.
    
    Parameters:
        ax (matplotlib.axes.Axes): the axes to adjust
        border_pad (float): horizontal padding beyond the axes
    """
    
    legend = ax.get_legend()
    if legend is not None:
        legend.set_bbox_to_anchor((1 + border_pad, 0), transform=ax.transAxes)
        legend._loc = 3
        legend.set_frame_on(True)
