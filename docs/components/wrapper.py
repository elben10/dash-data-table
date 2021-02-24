import dash_core_components as dcc
import dash_html_components as html

ID = "collapseID"


def wrapper(component, ctx={}):
    title = ctx["title"] if ctx.get("title") else "Home"
    routes = ctx["routes"] if ctx.get("routes") else []
    return [
        html.Nav(
            html.Div(
                [
                    toggle_button(ID),
                    dcc.Link(title, className="navbar-brand", href="/"),
                    html.Div(className="d-lg-none"),
                    navbar_items(routes, ID),
                ],
                className="container",
            ),
            className="navbar navbar-expand-lg navbar-light bg-light",
        ),
        html.Div(component, className="container"),
    ]


def toggle_button(target):
    return html.Button(
        html.Span(className="navbar-toggler-icon"),
        className="navbar-toggler",
        type="button",
        **{
            "data-toggle": "collapse",
            "data-target": f"#{target}",
            "aria-controls": target,
            "aria-expanded": False,
            "aria-label": "Toggle navigation",
        },
    )


def navbar_items(routes, target=""):
    if routes:
        return html.Div(
            html.Ul(
                [
                    html.Li(
                        dcc.Link(
                            route["title"], className="nav-link", href=route["path"]
                        ),
                        className="nav-item",
                    )
                    for route in routes
                    if route["navbar"]
                ],
                className="navbar-nav mr-auto mt-2 mt-lg-0",
            ),
            className="collapse navbar-collapse",
            id=target,
        )

