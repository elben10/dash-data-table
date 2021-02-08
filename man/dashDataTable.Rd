% Auto-generated: do not edit by hand
\name{dashDataTable}

\alias{dashDataTable}

\title{DashDataTable component}

\description{

}

\usage{
dashDataTable(id=NULL, containerClassName=NULL, containerStyle=NULL,
currentPage=NULL, currentRowsPerPage=NULL,
currentClickedRow=NULL, currentDoubleClickedRow=NULL,
currentSelectedRows=NULL, currentSorting=NULL, title=NULL,
columns=NULL, data=NULL, keyField=NULL, striped=NULL,
highlightOnHover=NULL, pointerOnHover=NULL, className=NULL,
style=NULL, responsive=NULL, disabled=NULL, overflowY=NULL,
overflowYOffset=NULL, dense=NULL, noTableHead=NULL,
persistTableHead=NULL, direction=NULL, selectableRows=NULL,
selectableRowsVisibleOnly=NULL,
selectableRowsHighlight=NULL,
selectableRowsNoSelectAll=NULL, sortServer=NULL,
expandableRows=NULL, expandOnRowClicked=NULL,
expandOnRowDoubleClicked=NULL,
expandableRowsHideExpander=NULL, defaultSortField=NULL,
defaultSortAsc=NULL, pagination=NULL, paginationServer=NULL,
paginationDefaultPage=NULL, paginationPerPage=NULL,
paginationRowsPerPageOptions=NULL, paginationTotalRows=NULL,
noHeader=NULL, fixedHeader=NULL,
fixedHeaderScrollHeight=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{containerClassName}{Character. Container className}

\item{containerStyle}{Named list. Container style}

\item{currentPage}{Numeric. Current page}

\item{currentRowsPerPage}{Numeric. Current rows per page}

\item{currentClickedRow}{Logical | numeric | character | named list | unnamed list. Current clicked row}

\item{currentDoubleClickedRow}{Logical | numeric | character | named list | unnamed list. Current double clicked row}

\item{currentSelectedRows}{List of logical | numeric | character | named list | unnamed lists. Current row selected}

\item{currentSorting}{Named list. Current sorting}

\item{title}{Character. Table title}

\item{columns}{List of named lists. Column definitions}

\item{data}{List of named lists. Row data}

\item{keyField}{Character. Key field the id that uniquely identifies the row}

\item{striped}{Logical. Stripe odd rows}

\item{highlightOnHover}{Logical. Highlight rows on hover}

\item{pointerOnHover}{Logical. Point icon on hover}

\item{className}{Character. Table className}

\item{style}{Named list. Style}

\item{responsive}{Logical. Horizontally scrollable}

\item{disabled}{Logical. Disable the table section}

\item{overflowY}{Logical. if a table is responsive, items such as 
layovers/menus/dropdowns will be clipped 
on the last row(s)}

\item{overflowYOffset}{Character. Used with overflowY}

\item{dense}{Logical. compact the rows}

\item{noTableHead}{Logical. Hides the sort columns}

\item{persistTableHead}{Logical. Show the table head event when progressPending is true}

\item{direction}{Character. Direction}

\item{selectableRows}{Logical. Selectable rows}

\item{selectableRowsVisibleOnly}{Logical. Select only visible rows
matters for pagination.
If this option is not set to
true it will select all 
rows specified in data also
those now shown}

\item{selectableRowsHighlight}{Logical. Highlight selected rows}

\item{selectableRowsNoSelectAll}{Logical. Show select all icon}

\item{sortServer}{Logical. Disables internal sorting}

\item{expandableRows}{Logical. Make rows expandable}

\item{expandOnRowClicked}{Logical. Expand rows on click}

\item{expandOnRowDoubleClicked}{Logical. Expand rows on double click}

\item{expandableRowsHideExpander}{Logical. Hide expander button}

\item{defaultSortField}{Character. Default pre sorting}

\item{defaultSortAsc}{Logical. Default pre sorting direction}

\item{pagination}{Logical. Enable pagination}

\item{paginationServer}{Logical. Use server side pagination}

\item{paginationDefaultPage}{Numeric. Start page}

\item{paginationPerPage}{Numeric. Rows per page}

\item{paginationRowsPerPageOptions}{List of numerics. Row per page options}

\item{paginationTotalRows}{Numeric. Total rows when using serverside pagination}

\item{noHeader}{Logical. No table header}

\item{fixedHeader}{Logical. Fixed header}

\item{fixedHeaderScrollHeight}{Character. Fixed header scroll height}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

