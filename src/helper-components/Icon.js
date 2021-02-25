import React from 'react';
import PropTypes from 'prop-types';
import {updateLocation} from './utils';

const Icon = (props) => {
    if (props.data.href) {
        return (
            <a
                href={props.data.href}
                onClick={(e) => updateLocation(e, props.data.href)}
            >
                <i className={props.data.icon} />
            </a>
        );
    }
    return <i className={props.data.icon} />;
};

Icon.defaultProps = {};
Icon.propTypes = {
    data: PropTypes.object,
};

export default Icon;
