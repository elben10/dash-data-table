import dash_core_components as dcc
import dash_html_components as html

from docs.components.wrapper import wrapper

CODE_EXAMPLE = """
from dash import Dash
from dash_data_table import DashDataTable

app = Dash(__name__)

columns = [
    {"name": "Column 1", "selector": "column1"}, 
    {"name": "Column 2", "selector": "column2"}, 
    {"name": "Column 3", "selector": "column3"}
]
data = [
    {"column1": "1", "column2": 2, "column3": "3"}, 
    {"column1": "1", "column2": 2, "column3": "3"}, 
    {"column1": "1", "column2": 2, "column3": "3"}
]

app.layout = DashDataTable(columns=columns, data=data)

if __name__ == "__main__":
    app.run_server()
""".strip()


def layout(ctx):
    return wrapper(
        [
            html.Div(
                html.Div(
                    [
                        html.H1("Dash Data Table", className="font-weight-light"),
                        html.P(
                            [
                                html.Em("Dash Data Table "),
                                "is an lightweight alternative to dash table. It is build upon ",
                                html.A(
                                    "react-data-table-component",
                                    href="https://www.npmjs.com/package/react-data-table-component",
                                ),
                            ],
                            style={"fontSize": "1.3rem", "fontWeight": 300},
                        ),
                    ],
                    className="col col-md-10 col-lg-8 col-xl-6 text-center",
                ),
                className="row justify-content-center pt-5",
            ),
            html.Hr(),
            html.Div(
                [
                    html.Div(
                        [
                            html.H2("Get started"),
                            html.P(
                                "Dash Data Table can easily be installed from pypi. Just "
                            ),
                            html.Pre(html.Code("pip install dash-data-table")),
                            html.P(
                                "After the package has been installed. We just need to the required stylesheets and scripts from bootstrap, and we are ready to get going.",
                                style={"fontSize": "1.2rem", "fontWeight": 250},
                            ),
                        ],
                        className="col-12 col-lg-6",
                    ),
                    html.Div(
                        [
                            dcc.Markdown(
                                "```bash\npip install dash-data-table\n```",
                                className="language-sh hljs mb-3",
                            ),
                            dcc.Markdown(
                                f"```python\n{CODE_EXAMPLE}\n```",
                                className="language-python hljs",
                            ),
                        ],
                        className="col-12 col-lg-6",
                    ),
                ],
                className="row",
            ),
        ],
        ctx,
    )
