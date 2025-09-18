import pandas as pd
import matplotlib.pyplot as plt

# funcs

from .data_loader import load_csv_all
from .data_loader import load_csv_range

from .data_cleaner import clean_data
from .data_cleaner import remove_char

from .data_transformer import pivot_data
from .data_transformer import round_up_to_nearest

from .data_visualisation import plot_histogram
from .data_visualisation import plot_scatter
from .data_visualisation import plot_line
from .data_visualisation import plot_multi_line

from .data_design import style_plot
from .data_design import style_title
from .data_design import style_line_annotation
from .data_design import design_lines
from .data_design import design_points
from .data_design import design_lines
from .data_design import expand_limits

__all__ = ['pd', 'plt', 'load_csv_all', 'load_csv_range', 'clean_data', 'remove_char', 'pivot_data', 'round_up_to_nearest', 'plot_histogram', 'plot_scatter', 
           'plot_line', 'plot_multi_line', 'style_plot', 'style_title', 'style_line_annotation', 'design_lines', 'design_points', 
           'design_lines', 'expand_limits']