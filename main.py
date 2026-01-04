from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.statistics_analysis import calculate_statistics, print_statistics
from src.clustering import clustering_analysis
from src.eda import plot_sales_trend, correlation_heatmap,correlation_plot,hit_flop_plot
from src.model import train_model
from src.utils import save_cleaned_data


def main():
    # Step 1: Load data
    df = load_data()

    # Step 2: Clean data
    df = clean_data(df)

    stats = calculate_statistics(df, "total_purchases")
    print_statistics(stats, "total_purchases")

    # Step 3: Save cleaned data
    save_cleaned_data(df)

    # Step 4: EDA plots
    plot_sales_trend(df)
    correlation_heatmap(df)
    correlation_plot(df)
    hit_flop_plot(df)

    # step 5: clustering model
    df, kmeans_model = clustering_analysis(df)

    # Step 6: Train ML model
    model ,mse = train_model(df)

    print("✅ Model trained successfully")
    print(f"📉 Mean Squared Error: {mse:.2f}")


if __name__ == "__main__":
    main()
