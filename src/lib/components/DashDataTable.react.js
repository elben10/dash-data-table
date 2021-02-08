import React, { Component } from 'react';
import PropTypes from 'prop-types';
import DataTable from 'react-data-table-component';
import { props } from 'ramda';

const ExpandedComponent = ({ data }) => <pre>{JSON.stringify(data, null, 2)}</pre>;

export default class DashDataTable extends Component {
    render() {
        return <div id={this.props.id} className={this.props.containerClassName} style={this.props.containerStyle}><DataTable
            title={this.props.title}
            columns={this.props.columns}
            data={this.props.data}
            keyField={this.props.keyField}
            striped={this.props.striped}
            highlightOnHover={this.props.highlightOnHover}
            pointerOnHover={this.props.pointerOnHover}
            className={this.props.className}
            style={this.props.style}
            responsive={this.props.responsive}
            disabled={this.props.disabled}
            overflowY={this.props.overflowY}
            overflowYOffset={this.props.overflowYOffset}
            dense={this.props.dense}
            noTableHead={this.props.noTableHead}
            persistTableHead={this.props.persistTableHead}
            direction={this.props.direction}
            selectableRows={this.props.selectableRows}
            selectableRowsVisibleOnly={this.props.selectableRowsVisibleOnly}
            selectableRowsHighlight={this.props.selectableRowsHighlight}
            selectableRowsNoSelectAll={this.props.selectableRowsNoSelectAll}
            expandableRows={this.props.expandableRows}
            expandOnRowClicked={this.props.expandOnRowClicked}
            expandOnRowDoubleClicked={this.props.expandOnRowDoubleClicked}
            expandableRowsHideExpander={this.props.expandableRowsHideExpander}
            expandableRowsComponent={<ExpandedComponent />}
            defaultSortField={this.props.defaultSortField}
            defaultSortAsc={this.props.defaultSortAsc}
            sortServer={this.props.sortServer}
            pagination={this.props.pagination}
            paginationServer={this.props.paginationServer}
            paginationDefaultPage={this.props.paginationDefaultPage}
            paginationPerPage={this.props.paginationPerPage}
            paginationRowsPerPageOptions={this.props.paginationRowsPerPageOptions}
            paginationTotalRows={this.props.paginationTotalRows}
            noHeader={this.props.noHeader}
            fixedHeader={this.props.fixedHeader}
            fixedHeaderScrollHeight={this.props.fixedHeaderScrollHeight}
            onChangePage={currentPage => this.props.setProps({ currentPage })}
            onChangeRowsPerPage={(currentRowsPerPage, currentPage) => this.props.setProps({ currentRowsPerPage, currentPage })}
            onRowClicked={(row) => this.props.setProps({ currentClickedRow: row[this.props.keyField || 'id'] })}
            onRowDoubleClicked={(row) => this.props.setProps({ currentDoubleClickedRow: row[this.props.keyField || 'id'] })}
            onSelectedRowsChange={(row) => this.props.setProps({ currentSelectedRows: row.selectedRows.map(elem => elem[this.props.keyField || 'id']) })}
            onSort={(column, sortDirection) => this.props.setProps({ currentSorting: { column, sortDirection } })}
        /></div>
    }
}

DashDataTable.defaultProps = {
    pagination: true,
};

DashDataTable.propTypes = {

    // ****************************
    //   Dash Properties 
    // ****************************

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
    /**
     * Container className
     */
    containerClassName: PropTypes.string,
    /**
     * Container style
     */
    containerStyle: PropTypes.object,
    /**
     * Current page
     */
    currentPage: PropTypes.number,
    /**
     * Current rows per page
     */
    currentRowsPerPage: PropTypes.number,
    /**
     * Current clicked row
     */
    currentClickedRow: PropTypes.any,
    /**
     * Current double clicked row
     */
    currentDoubleClickedRow: PropTypes.any,
    /**
     * Current row selected
     */
    currentSelectedRows: PropTypes.arrayOf(PropTypes.any),
    /**
     * Current sorting
     */
    currentSorting: PropTypes.object,

    // ****************************
    //   Basic Properties
    // ****************************

    /**
     * Table title
     */
    title: PropTypes.string,

    /**
     * Column definitions
     */
    columns: PropTypes.arrayOf(PropTypes.object).isRequired,
    /**
     * Row data
     */
    data: PropTypes.arrayOf(PropTypes.object),
    /**
     * Key field the id that uniquely identifies the row
     */
    keyField: PropTypes.string,
    /**
     * Stripe odd rows
     */
    striped: PropTypes.bool,
    /**
     * Highlight rows on hover
     */
    highlightOnHover: PropTypes.bool,
    /**
     * Point icon on hover
     */
    pointerOnHover: PropTypes.bool,
    /**
     * Table className
     */
    className: PropTypes.string,
    /**
     * Style
     */
    style: PropTypes.object,
    /**
     * Horizontally scrollable
     */
    responsive: PropTypes.bool,
    /**
     * Disable the table section
     */
    disabled: PropTypes.bool,
    /**
     * if a table is responsive, items such as 
     * layovers/menus/dropdowns will be clipped 
     * on the last row(s)
     */
    overflowY: PropTypes.bool,
    /**
     * Used with overflowY
     */
    overflowYOffset: PropTypes.string,
    /**
     * compact the rows
     */
    dense: PropTypes.bool,
    /**
     * Hides the sort columns
     */
    noTableHead: PropTypes.bool,
    /**
     * Show the table head event when progressPending is true
     */
    persistTableHead: PropTypes.bool,
    /**
     * Direction
     */
    direction: PropTypes.string,

    // ****************************
    //   Row Selection Properties
    // ****************************

    /**
     * Selectable rows
     */
    selectableRows: PropTypes.bool,
    /**
     * Select only visible rows
     * matters for pagination.
     * If this option is not set to
     * true it will select all 
     * rows specified in data also
     * those now shown
     */
    selectableRowsVisibleOnly: PropTypes.bool,
    /**
     * Highlight selected rows
     */
    selectableRowsHighlight: PropTypes.bool,
    /**
     * Show select all icon
     */
    selectableRowsNoSelectAll: PropTypes.bool,
    /**
     * Disables internal sorting
     */
    sortServer: PropTypes.bool,

    // ****************************
    //   Row Expander Properties
    // ****************************

    /**
     * Make rows expandable
     */
    expandableRows: PropTypes.bool,
    /**
     * Expand rows on click
     */
    expandOnRowClicked: PropTypes.bool,
    /** 
     * Expand rows on double click
    */
    expandOnRowDoubleClicked: PropTypes.bool,
    /**
     * Hide expander button
     */
    expandableRowsHideExpander: PropTypes.bool,

    // ****************************
    //   Sorting Properties
    // ****************************

    /**
     * Default pre sorting 
     */
    defaultSortField: PropTypes.string,
    /**
     * Default pre sorting direction
     */
    defaultSortAsc: PropTypes.bool,

    // ****************************
    //   Pagination Properties
    // ****************************

    /**
     * Enable pagination
     */
    pagination: PropTypes.bool,
    /**
     * Use server side pagination
     */
    paginationServer: PropTypes.bool,
    /**
     * Start page
     */
    paginationDefaultPage: PropTypes.number,
    /**
     * Rows per page
     */
    paginationPerPage: PropTypes.number,
    /**
     * Row per page options
     */
    paginationRowsPerPageOptions: PropTypes.arrayOf(PropTypes.number),
    /**
     * Total rows when using serverside pagination
     */
    paginationTotalRows: PropTypes.number,

    // ****************************
    //   Header Properties
    // ****************************

    /**
     * No table header
     */
    noHeader: PropTypes.bool,
    /**
     * Fixed header
     */
    fixedHeader: PropTypes.bool,
    /**
     * Fixed header scroll height
     */
    fixedHeaderScrollHeight: PropTypes.string,
};
