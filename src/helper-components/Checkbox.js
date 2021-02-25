import React from 'react';
import PropTypes from 'prop-types';

const Checkbox = (props) => {
    return (
        <input
            type="checkbox"
            aria-label="Checkbox for following text input"
            defaultChecked={props.data}
            onClick={(e) => e.preventDefault()}
        />
    );
};

Checkbox.defaultProps = {};
Checkbox.propTypes = {
    data: PropTypes.bool,
};

export default Checkbox;
