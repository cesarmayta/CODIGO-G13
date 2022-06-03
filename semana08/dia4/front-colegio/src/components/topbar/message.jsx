import React from 'react';
import { Link } from "react-router-dom";
import { Dropdown } from 'react-bootstrap';

const TopbarUserMessage = () => {

    return (
            <Dropdown as="li"  className={`icons-dropdown d-none-m`} id="topbar-message-menu">
                <Dropdown.Toggle as={Link} to="#noty">
                    <i className="far fa-envelope"></i>
                    <div className="ml-2 notify setpos"> <span className="heartbit" /> 
                        <span className="point" /> 
                    </div>
                </Dropdown.Toggle>
                <Dropdown.Menu className={`top-dropdown lg-dropdown notification-dropdown`}>
                    <Dropdown.Header as='div'>
                        <Link className="float-right" to="#be"><small>View All</small></Link> Messages
                    </Dropdown.Header>
                    <div className="scrollDiv">
                    <div className="notification-list">
                        <Dropdown.Item as={Link} className="clearfix" to="#be">
                            <span className="notification-icon">
                                <img alt="" className="rounded-circle" src="/assets/img/avtar-2.png" width={50} />
                            </span> 
                            <span className="notification-title">
                                John Doe 
                                <label className="label label-warning float-right">Support</label>
                            </span> 
                            <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span> 
                            <span className="notification-time">15 minutes ago</span>
                        </Dropdown.Item>
                        <Dropdown.Item as={Link} className="clearfix" to="#be">
                        <span className="notification-icon">
                            <img alt="" className="rounded-circle" src="/assets/img/avtar-3.png" width={50} />
                        </span> 
                        <span className="notification-title">
                            Govindo Doe 
                            <label className="label label-warning float-right">Support</label>
                        </span> 
                        <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span> 
                        <span className="notification-time">15 minutes ago</span>
                        </Dropdown.Item> 
                        <Dropdown.Item as={Link} className="clearfix" to="#be">
                        <span className="notification-icon">
                            <img alt="" className="rounded-circle" src="/assets/img/avtar-4.png" width={50} />
                        </span> 
                        <span className="notification-title">
                            Megan Doe 
                            <label className="label label-warning float-right">Support</label>
                        </span>
                        <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                        <span className="notification-time">15 minutes ago</span>
                        </Dropdown.Item> 
                        <Dropdown.Item as={Link} className="clearfix" to="#be">
                        <span className="notification-icon">
                            <img alt="" className="rounded-circle" src="/assets/img/avtar-5.png" width={50} />
                        </span>
                        <span className="notification-title">
                            Hritik Doe 
                            <label className="label label-warning float-right">Support</label>
                        </span>
                        <span className="notification-description">Lorem Ipsum is simply dummy text of the printing.</span>
                        <span className="notification-time">15 minutes ago</span>
                        </Dropdown.Item>
                    </div>
                </div>
            </Dropdown.Menu>
        </Dropdown>
    );
}

export default TopbarUserMessage;