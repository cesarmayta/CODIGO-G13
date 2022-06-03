import React from 'react';
import { Row, Col, Tab, Nav, Button } from 'react-bootstrap';
import './style.scss';
import ColorAction from './color-action'
import Configuration from './configuration';
import LayoutAction from './layout-action'
import UserConfig from './Config';
// ES6 Imports
// import * as Scroll from 'react-scroll';
// import { Link, Element, Events, animateScroll as scroll, scrollSpy, scroller } from 'react-scroll'

class Customizer extends React.Component{

    constructor(props) {
        super(props);
        this.state = {
            show: false,
        }
        this.show = this.show.bind(this);
        this.hide = this.hide.bind(this);        
    }

    show(){
        this.setState({ show: true });
    }
    
    hide(){
        this.setState({ show: false });
    }
    
    render() {
        return (
            <React.Fragment>
                <div id="customizer" className={this.state.show?'show':'hide'}>
                    <UserConfig />
                    <Tab.Container id="customizer-tabs" defaultActiveKey="first">
                        <Row>
                            <Col sm={3} className="d-flex align-items-center">
                                <Nav variant="pills" className="flex-column">
                                    <Nav.Item>
                                    <Nav.Link eventKey="first" onClick={this.show}>
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-sliders">
                                            <line x1="4" y1="21" x2="4" y2="14"></line>
                                            <line x1="4" y1="10" x2="4" y2="3"></line>
                                            <line x1="12" y1="21" x2="12" y2="12"></line>
                                            <line x1="12" y1="8" x2="12" y2="3"></line>
                                            <line x1="20" y1="21" x2="20" y2="16"></line>
                                            <line x1="20" y1="12" x2="20" y2="3"></line>
                                            <line x1="1" y1="14" x2="7" y2="14"></line>
                                            <line x1="9" y1="8" x2="15" y2="8"></line>
                                            <line x1="17" y1="16" x2="23" y2="16"></line>
                                        </svg>
                                    </Nav.Link>
                                    </Nav.Item>
                                    <Nav.Item>
                                    <Nav.Link eventKey="second" onClick={this.show}>
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-moon">
                                            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                                        </svg>
                                    </Nav.Link>
                                    </Nav.Item>
                                </Nav>
                            </Col>
                            <Col sm={9}>
                                <Tab.Content>
                                    <div className="customizer-header">
                                        <Button variant="link" size="sm" className="close-customer-btn" onClick={this.hide}>
                                            <span className="icon-close"></span>
                                        </Button>
                                        
                                        <h5>Customizer</h5>
                                        <p class="mb-0">Customize &amp; Preview Real Time</p>
                                        <span>Customizer action are comming soon</span>
                                        <Configuration />
                                    </div>
                                    <hr/>
                                    <Tab.Pane eventKey="first">
                                        <LayoutAction />
                                    </Tab.Pane>
                                    <Tab.Pane eventKey="second">
                                        <ColorAction />
                                    </Tab.Pane>
                                </Tab.Content>
                            </Col>
                        </Row>
                    </Tab.Container>
                </div>
            </React.Fragment>
        );
    }

}



export default Customizer;