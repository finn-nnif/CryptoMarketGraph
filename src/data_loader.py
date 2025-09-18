import pandas as pd

def load_csv_all(filepath: str) -> pd.DataFrame:
    """
    Load entire CSV file into a DataFrame.
    """
    return pd.read_csv(filepath)


def load_csv_range(filepath: str, min_row: int, max_row: int) -> pd.DataFrame:
    """
    Load rows between min_row and max_row (inclusive) from CSV.

    Parameters:
        filepath (str): Path to CSV file
        min_row (int): Starting row index (0-based, inclusive)
        max_row (int): Ending row index (0-based, inclusive)

    Returns:
        pd.DataFrame: DataFrame with selected rows
    """
    if max_row < min_row:
        raise ValueError("max_row must be greater than or equal to min_row")

    with open(filepath, 'r') as f:
        total_rows = sum(1 for _ in f)

    data_rows = total_rows - 1

    if min_row > data_rows:
        raise ValueError(f"min_row ({min_row}) exceeds number of data rows ({data_rows})")

    if max_row > data_rows:
        print(f"Warning: max_row ({max_row}) exceeds number of data rows ({data_rows}), adjusting max_row to {data_rows}")
        max_row = data_rows

    nrows = max_row - min_row + 1
    skiprows = list(range(1, min_row + 1)) if min_row > 0 else None

    df = pd.read_csv(filepath, skiprows=skiprows, nrows=nrows)
    return df