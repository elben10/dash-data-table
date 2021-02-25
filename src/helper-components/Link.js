import React from 'react';
import PropTypes from 'prop-types';
import {updateLocation} from './utils';

const Link = (props) => {
    return (
        <a
            href={props.data.href}
            onClick={(e) => updateLocation(e, props.data.href)}
        >
            {props.data.text}
        </a>
    );
};

Link.defaultProps = {};
Link.propTypes = {
    data: PropTypes.object,
};

export default Link;
