import React, { Component } from 'react';
import PropTypes from 'prop-types';
import DataTable from 'react-data-table-component';
import Expanded from '../helper-components/Expanded'

const DashDataTable = (props) => {
        return <div id={props.id} className={props.containerClassName} style={props.containerStyle}><DataTable
            title={props.title}
            columns={props.columns}
            data={props.data}
            keyField={props.keyField}
            striped={props.striped}
            highlightOnHover={props.highlightOnHover}
            pointerOnHover={props.pointerOnHover}
            className={props.className}
            style={props.style}
            responsive={props.responsive}
            disabled={props.disabled}
            overflowY={props.overflowY}
            overflowYOffset={props.overflowYOffset}
            dense={props.dense}
            noTableHead={props.noTableHead}
            persistTableHead={props.persistTableHead}
            direction={props.direction}
            selectableRows={props.selectableRows}
            selectableRowsVisibleOnly={props.selectableRowsVisibleOnly}
            selectableRowsHighlight={props.selectableRowsHighlight}
            selectableRowsNoSelectAll={props.selectableRowsNoSelectAll}
            expandableRows={props.expandableRows}
            expandOnRowClicked={props.expandOnRowClicked}
            expandOnRowDoubleClicked={props.expandOnRowDoubleClicked}
            expandableRowsHideExpander={props.expandableRowsHideExpander}
            expandableRowsComponent={<Expanded />}
            defaultSortField={props.defaultSortField}
            defaultSortAsc={props.defaultSortAsc}
            sortServer={props.sortServer}
            pagination={props.pagination}
            paginationServer={props.paginationServer}
            paginationDefaultPage={props.paginationDefaultPage}
            paginationPerPage={props.paginationPerPage}
            paginationRowsPerPageOptions={props.paginationRowsPerPageOptions}
            paginationTotalRows={props.paginationTotalRows}
            noHeader={props.noHeader}
            fixedHeader={props.fixedHeader}
            fixedHeaderScrollHeight={props.fixedHeaderScrollHeight}
            onChangePage={currentPage => props.setProps({ currentPage })}
            onChangeRowsPerPage={(currentRowsPerPage, currentPage) => props.setProps({ currentRowsPerPage, currentPage })}
            onRowClicked={(row) => props.setProps({ currentClickedRow: row[props.keyField || 'id'] })}
            onRowDoubleClicked={(row) => props.setProps({ currentDoubleClickedRow: row[props.keyField || 'id'] })}
            onSelectedRowsChange={(row) => props.setProps({ currentSelectedRows: row.selectedRows.map(elem => elem[props.keyField || 'id']) })}
            onSort={(column, sortDirection) => props.setProps({ currentSorting: { column, sortDirection } })}
        /></div>
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
