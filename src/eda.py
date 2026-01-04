import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(df):
    plt.figure()
    sns.lineplot(x="week_number", y="search_purchases", data=df)
    plt.title("Search Purchases Over Time")
    plt.xlabel("Week Number")
    plt.ylabel("Purchases")
    plt.tight_layout()
    plt.show()


def correlation_heatmap(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap (Numeric Features Only)")
    plt.tight_layout()
    plt.show()

def correlation_plot(df):
    """
    Create a correlation heatmap for numeric features
    """
    # Select numeric columns only
    numeric_df = df.select_dtypes(include=["number"])

    plt.figure(figsize=(10, 6))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap of Marketing Features")
    plt.tight_layout()
    plt.show()

def hit_flop_plot(df):
    """
    Plot Hit vs Flop count based on performance column
    """
    plt.figure(figsize=(6, 4))

    sns.countplot(
        x="performance",
        data=df
    )

    plt.title("Hit vs Flop Distribution")
    plt.xlabel("Performance")
    plt.ylabel("Number of Campaigns")
    plt.tight_layout()
    plt.show()
