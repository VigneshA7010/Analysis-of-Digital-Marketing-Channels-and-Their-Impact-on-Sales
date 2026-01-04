import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop unwanted column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Fill missing values
    df = df.ffill()

    # Convert numeric columns safely
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Create total purchases
    df["total_purchases"] = (
        df["search_purchases"]
        + df["ad_purchases"]
        + df["social_purchases"]
    )

    # Classification: Hit / Flop
    avg_purchase = df["total_purchases"].mean()
    df["performance"] = df["total_purchases"].apply(
        lambda x: "Hit" if x >= avg_purchase else "Flop"
    )

    return df
