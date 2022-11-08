import plotly.express as px
from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Restaurant tips by day of week"),
        dcc.Dropdown(
            id="dropdown",
            options=["Fri", "Sat", "Sun"],
            value="Fri",
            clearable=False,
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(Output("graph", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    df = px.data.tips()  # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
