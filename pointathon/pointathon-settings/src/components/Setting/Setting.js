import React from 'react';
import PropTypes from 'prop-types';
import styles from './Setting.css';

const Setting = props => (
	<div>
		This is a component called Setting.
		<input type="text" id="newTextBox" />
	</div>
);

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
// class Setting extends React.Component {
//   render() {
//     return <div>This is a component called Setting.</div>;
//   }
// }

const SettingPropTypes = {
	// always use prop types!
};

Setting.propTypes = SettingPropTypes;

export default Setting;
