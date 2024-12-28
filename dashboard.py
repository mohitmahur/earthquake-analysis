import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Load datasets
file_path_1 = "earthquake_1995-2023.csv"
file_path_2 = "earthquake_data.csv"

try:
    earthquake_data_1 = pd.read_csv(file_path_1)
    earthquake_data_2 = pd.read_csv(file_path_2)
except FileNotFoundError:
    raise Exception("One or both datasets are not found. Please check file paths.")

# Standardize and merge datasets
earthquake_data_1.columns = earthquake_data_1.columns.str.strip()
earthquake_data_2.columns = earthquake_data_2.columns.str.strip()

merged_data = pd.merge(
    earthquake_data_1,
    earthquake_data_2,
    how="inner",
    on=["latitude", "longitude", "magnitude"]
)

merged_data.columns = merged_data.columns.str.lower()
merged_data.rename(
    columns={"depth_x": "depth", "sig_x": "sig", "tsunami_x": "tsunami"},
    inplace=True
)

merged_data.dropna(subset=["magnitude", "depth"], inplace=True)
high_risk_zones = merged_data[(merged_data["magnitude"] > 6.0) & (merged_data["tsunami"] == 1)]

# Initialize Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE],  
    suppress_callback_exceptions=True
)
app.title = "Earthquake Dashboard"

# Styling
header_style = {
    "background": "#343a40",
    "color": "#f8f9fa",
    "padding": "0.5rem",
    "text-align": "center",
    "font-size": "2rem",
    "font-family": "Arial, sans-serif",
    "box-shadow": "0px 4px 10px rgba(186, 88, 88, 0.2)"
}

tab_style = {
    "padding": "0.8rem",
    "font-size": "1rem",
    "color": "#adb5bd",
    "background": "#495057",
    "border-radius": "5px",
    "text-align": "center",
}

selected_tab_style = {
    "padding": "0.8rem",
    "font-size": "1rem",
    "color": "#f8f9fa",
    "background": "#007bff",
    "border-radius": "5px",
    "text-align": "center",
}

card_style = {
    "margin": "1rem",
    "padding": "1rem",
    "box-shadow": "0px 2px 8px rgba(0, 0, 0, 0.1)",
    "border-radius": "10px",
    "background": "#212529",
}

footer_style = {
    "text-align": "center",
    "color": "#adb5bd",
    "font-size": "1rem",
    "padding": "1rem",
    "border-top": "1px solid #343a40",
    "margin-top": "2rem",
}

# App layout
app.layout = dbc.Container(
    fluid=True,
    children=[
        # Header
        dbc.Row(
            dbc.Col(html.H1("Earthquake Analysis Dashboard", style=header_style))
        ),

        # Tabs
        dbc.Row(
            dbc.Col(
                dcc.Tabs(
                    id="tabs",
                    className="nav nav-tabs",
                    children=[
                        dcc.Tab(
                            label="Global Map",
                            style=tab_style,
                            selected_style=selected_tab_style,
                            children=[
                                dbc.Card(
                                    dbc.CardBody(
                                        dcc.Graph(
                                            id="global-map",
                                            style={"height": "140vh"},
                                            figure=px.scatter_mapbox(
                                                merged_data,
                                                lat="latitude",
                                                lon="longitude",
                                                size="magnitude",
                                                color="magnitude",
                                                hover_data=["latitude", "longitude", "depth", "magnitude"],
                                                zoom=1,
                                                title="Global Earthquake Distribution (1995-2023)",
                                                mapbox_style="open-street-map",
                                                size_max=19,
                                                color_continuous_scale="Turbo"
                                            )
                                        )
                                    ),
                                    style=card_style
                                )
                            ]
                        ),
                        dcc.Tab(
                            label="High-Risk Zones",
                            style=tab_style,
                            selected_style=selected_tab_style,
                            children=[
                                dbc.Card(
                                    dbc.CardBody(
                                        dcc.Graph(
                                            id="high-risk-map",
                                            style={"height": "80vh"},
                                            figure=px.scatter(
                                                high_risk_zones,
                                                x="longitude",
                                                y="latitude",
                                                size="magnitude",
                                                color="magnitude",
                                                hover_data=["latitude", "longitude", "magnitude", "tsunami"],
                                                title="High-Seismicity and Tsunami-Prone Zones",
                                                template="plotly_dark",
                                                color_continuous_scale="Plasma"
                                            )
                                        )
                                    ),
                                    style=card_style
                                )
                            ]
                        ),
                        dcc.Tab(
                            label="Correlation Analysis",
                            style=tab_style,
                            selected_style=selected_tab_style,
                            children=[
                                dbc.Card(
                                    dbc.CardBody(
                                        dcc.Graph(
                                            id="correlation-heatmap",
                                            style={"height": "80vh"},
                                            figure=px.imshow(
                                                merged_data[["magnitude", "depth", "sig"]].corr(),
                                                text_auto=True,
                                                title="Correlation Heatmap of Earthquake Metrics",
                                                template="plotly_dark",
                                                color_continuous_scale="Viridis"
                                            )
                                        )
                                    ),
                                    style=card_style
                                )
                            ]
                        )
                    ]
                )
            )
        ),

        # Footer
        dbc.Row(
            dbc.Col(
                html.Footer(
                    "© 2024 Mohit Mahur | All Rights Reserved",
                    style=footer_style
                )
            )
        )
    ]
)

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
