import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def clustering_analysis(df):
    """
    Perform K-Means clustering on marketing data
    """

    # Features for clustering
    features = [
        "search_sessions",
        "ad_clicks",
        "social_views",
        "ad_budget",
        "total_purchases"
    ]

    X = df[features]

    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means
    kmeans = KMeans(n_clusters=2, random_state=42)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    # Plot clusters
    plt.figure(figsize=(7, 5))
    sns.scatterplot(
        x=df["ad_budget"],
        y=df["total_purchases"],
        hue=df["cluster"],
        palette="Set1"
    )

    plt.title("K-Means Clustering of Marketing Campaigns")
    plt.xlabel("Ad Budget")
    plt.ylabel("Total Purchases")
    plt.tight_layout()
    plt.show()

    return df, kmeans
