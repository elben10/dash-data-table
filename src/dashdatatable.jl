
module DashDataTable
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("dashdatatable.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_data_table",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_data_table.min.js",
    external_url = "https://unpkg.com/dash_data_table@0.0.1/dash_data_table/dash_data_table.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_data_table.min.js.map",
    external_url = "https://unpkg.com/dash_data_table@0.0.1/dash_data_table/dash_data_table.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end