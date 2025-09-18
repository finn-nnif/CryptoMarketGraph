import pandas as pd

def clean_data(df, drop_duplicates=True):
    if drop_duplicates:
        df.drop_duplicates(inplace=True)
    
    df.dropna(inplace=True)
    return df

def remove_char(df, column_name, symbol):
    """
    Remove all occurrences of a specified symbol (string) from the given column in the DataFrame.

    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the column to clean.
    column_name : str
        The name of the column to process.
    symbol : str
        The symbol or substring to remove from the column values.

    Returns:
    --------
    pandas.DataFrame
        The DataFrame with the cleaned column.
    """
    df[column_name] = df[column_name].astype(str).str.replace(symbol, '', regex=False)
    return df