
import numpy as np

def pivot_data(df, index_col, columns_col, values_col):
    return df.pivot(index=index_col, columns=columns_col, values=values_col)

def round_up_to_nearest(x):
    magnitude = 10 ** (len(str(int(x))) - 1)
    rounded = np.ceil(x / magnitude) * magnitude
    return rounded