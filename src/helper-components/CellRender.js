import React from "react";
import PropTypes from "prop-types";
import Button from "./Button";
import BadgeList from "./BadgeList";
import Checkbox from "./Checkbox";
import Icon from "./Icon";
import Link from "./Link";

const CellRender = (props) => {
  if (props.column.type === "button") {
    return <Button data={props.row[props.column.selector]} />;
  } else if (props.column.type === "badgeList") {
    return <BadgeList data={props.row[props.column.selector]} />;
  } else if (props.column.type === "checkbox") {
    return <Checkbox data={props.row[props.column.selector]} />;
  } else if (props.column.type === "icon") {
    return <Icon data={props.row[props.column.selector]} />;
  } else if (props.column.type === "link") {
    return <Link data={props.row[props.column.selector]} />;
  }
  throw Error(`The type "${props.column.type}" is not supported.`);
};

CellRender.defaultProps = {};
CellRender.propTypes = {
  column: PropTypes.object,
  row: PropTypes.object,
};

export default CellRender;
