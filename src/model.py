from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(df):
    df["total_purchases"] = (
        df["search_purchases"] +
        df["ad_purchases"] +
        df["social_purchases"]
    )

    features = [
        "search_sessions",
        "ad_clicks",
        "social_views",
        "ad_budget"
    ]

    X = df[features]
    y = df["total_purchases"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    return model, mse
