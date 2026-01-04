import plotly.express as px

def sales_trend_figure(df):
    return px.line(
        df,
        x="week_number",
        y="search_purchases",
        title="Search Purchases Over Time"
    )


def correlation_heatmap_figure(df):
    numeric_df = df.select_dtypes(include="number")
    return px.imshow(
        numeric_df.corr(),
        title="Correlation Heatmap",
        aspect="auto"
    )
