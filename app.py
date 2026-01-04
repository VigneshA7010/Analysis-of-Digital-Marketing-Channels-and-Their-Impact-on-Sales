from dash import Dash, dcc, html

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.eda_dash import sales_trend_figure, correlation_heatmap_figure
from src.model import train_model

# Load & clean
df = clean_data(load_data())

# Train model (optional in Dash)
model, mse = train_model(df)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("📊 Marketing Dashboard"),

        html.P(f"Model MSE: {mse:.2f}"),

        dcc.Graph(figure=sales_trend_figure(df)),
        dcc.Graph(figure=correlation_heatmap_figure(df))
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
