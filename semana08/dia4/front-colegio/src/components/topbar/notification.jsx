import React from 'react';
import { Link } from "react-router-dom";
import { Dropdown } from 'react-bootstrap';

class TopbarUserNotification extends React.Component {

  render() {
    return (
      <React.Fragment>
        <Dropdown as="li" className="icons-dropdown d-none-m">
          <Dropdown.Toggle as="a" href="#be" id="topbar-notification-menu">
              <i className="fa fa-bell" /> 
              <div className="ml-2 notify setpos"> <span className="heartbit" /> 
                  <span className="point" /> 
              </div>
          </Dropdown.Toggle>
          <Dropdown.Menu as='ul' className={`top-dropdown lg-dropdown notification-dropdown`}>
            <li>
              <Dropdown.Header>
                <Link className="float-right" href="#be"><small>View All</small></Link> Notifications
              </Dropdown.Header>
              <div className="scrollDiv">
                <div className="notification-list">
                    <a className="clearfix" href="#be">
                      <span className="notification-icon">
                          <i className="icon-cloud-upload text-primary" />
                      </span>
                      <span className="notification-title">Upload Complete</span> 
                      <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                      <span className="notification-time">15 minutes ago</span>
                    </a> 
                    <a className="clearfix" href="#be">
                    <span className="notification-icon">
                        <i className="icon-info text-warning" />
                    </span>
                    <span className="notification-title">Storage Space low</span>
                    <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                    <span className="notification-time">15 minutes ago</span>
                    </a>
                    <a className="clearfix" href="#be">
                    <span className="notification-icon">
                        <i className="icon-check text-success" />
                    </span>
                    <span className="notification-title">Project Task Complete</span>
                    <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                    <span className="notification-time">15 minutes ago</span>
                    </a>
                    <a className="clearfix" href="#be">
                    <span className="notification-icon">
                        <i className=" icon-graph text-danger" />
                    </span>
                    <span className="notification-title">CPU Usage</span>
                    <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                    <span className="notification-time">15 minutes ago</span>
                    </a>
                </div>
                </div>
            </li>
          </Dropdown.Menu>
        </Dropdown>
      </React.Fragment>
    );
  }
}

export default TopbarUserNotification;