import React from 'react';
import PropTypes from 'prop-types';

const Expanded = ({data}) => <pre>{JSON.stringify(data, null, 2)}</pre>;
Expanded.propTypes = {
    data: PropTypes.any,
};

export default Expanded;
