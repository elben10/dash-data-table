import React from 'react';
import PropTypes from 'prop-types';
import {updateLocation, randomID} from './utils';

const BadgeList = (props) => {
    return (
        <div className="pb-1 pt-1">
            {props.data.map((elem) => {
                if (elem.href) {
                    return (
                        <a
                            key={randomID()}
                            href={elem.href}
                            onClick={(e) => updateLocation(e, elem.href)}
                            className={`badge badge-pill badge-${
                                elem.color || 'primary'
                            }`}
                        >
                            {elem.text}
                        </a>
                    );
                }
                return (
                    <span
                        key={randomID()}
                        className={`badge badge-pill badge-${
                            elem.color || 'primary'
                        }`}
                    >
                        {elem.text}
                    </span>
                );
            })}
        </div>
    );
};

BadgeList.defaultProps = {};
BadgeList.propTypes = {
    data: PropTypes.arrayOf(PropTypes.object),
};

export default BadgeList;
