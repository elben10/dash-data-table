import React from 'react';
import PropTypes from 'prop-types';
import {updateLocation} from './utils';

const Button = (props) => {
    if (props.data.href) {
        return (
            <a
                href={props.data.href}
                onClick={(e) => updateLocation(e, props.data.href)}
            >
                <button className="btn btn-sm btn-primary">
                    {props.data.text}
                </button>
            </a>
        );
    }
    return (
        <button className="btn btn-sm btn-primary">
            {props.data.text}
        </button>
    );
};

Button.defaultProps = {};
Button.propTypes = {
    data: PropTypes.object,
};

export default Button;
