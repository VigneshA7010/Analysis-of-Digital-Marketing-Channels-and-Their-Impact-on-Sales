from pathlib import Path

def save_cleaned_data(df):
    output_path = Path("data/processed/cleaned_marketing.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
