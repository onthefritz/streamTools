import React from 'react';
import { shallow, render, mount } from 'enzyme';
import Setting from './Setting';

describe('Setting', () => {
  let props;
  let shallowSetting;
  let renderedSetting;
  let mountedSetting;

  const shallowTestComponent = () => {
    if (!shallowSetting) {
      shallowSetting = shallow(<Setting {...props} />);
    }
    return shallowSetting;
  };

  const renderTestComponent = () => {
    if (!renderedSetting) {
      renderedSetting = render(<Setting {...props} />);
    }
    return renderedSetting;
  };

  const mountTestComponent = () => {
    if (!mountedSetting) {
      mountedSetting = mount(<Setting {...props} />);
    }
    return mountedSetting;
  };  

  beforeEach(() => {
    props = {};
    shallowSetting = undefined;
    renderedSetting = undefined;
    mountedSetting = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
