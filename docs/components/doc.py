import dash_html_components as html


def doc_generator(metadata, component):
    component_metadata = metadata[component]
    return html.Div(
        [
            html.H1(component_metadata["displayName"], className="font-weight-light"),
            html.Ul(
                [html.Li([html.Code(name), html.Span(f" ({prop['type']['name']}): {prop['description']}")], style={"fontSize": "1rem"}) for name, prop in component_metadata["props"].items()],
                className="list-unstyled",
            ),
        ],
    )
