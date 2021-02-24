import dash_core_components as dcc
import dash_html_components as html

DEFAULT_IMAGE = "https://images.unsplash.com/photo-1555861496-0666c8981751?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2550&q=80"


def gallery(items):
    return html.Div([gallery_item(item) for item in items], className="row")


def gallery_item(item):
    return html.Div(
        html.Div(
            [
                html.Img(
                    src=item.get("img", DEFAULT_IMAGE,),
                    className="img-fluid card-img-top",
                ),
                html.Div(
                    [
                        html.H5(
                            dcc.Link(item.get("title"), href="/", className="text-dark")
                        ),
                        html.P(
                            item.get("description"), className="small text-muted mb-0",
                        ),
                        dcc.Link(
                            html.P("Go to example", className="mb-0"),
                            className="d-flex align-items-center justify-content-center rounded-pill bg-light px-3 py-2 mt-4",
                            href=item.get("href"),
                        ),
                    ],
                    className="p-4",
                ),
            ],
            className="bg-white rounded shadow-sm",
        ),
        className="col-xl-3 col-lg-4 col-md-6 mb-4",
    )
