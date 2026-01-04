import pandas as pd


def calculate_statistics(df: pd.DataFrame, column: str) -> dict:
    """
    Calculate mean, median, mode, and standard deviation
    for a given numeric column.
    """

    stats = {}

    stats["mean"] = df[column].mean()
    stats["median"] = df[column].median()
    stats["mode"] = df[column].mode()[0]
    stats["std_dev"] = df[column].std()

    return stats


def print_statistics(stats: dict, column: str):
    """
    Print statistics in a clean format
    """

    print(f"\n📊 Statistical Analysis for '{column}'")
    print("-" * 40)
    print(f"Mean               : {stats['mean']:.2f}")
    print(f"Median             : {stats['median']:.2f}")
    print(f"Mode               : {stats['mode']:.2f}")
    print(f"Standard Deviation : {stats['std_dev']:.2f}")
