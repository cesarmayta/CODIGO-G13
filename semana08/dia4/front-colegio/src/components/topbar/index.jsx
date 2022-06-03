import React from 'react';
import { Link } from "react-router-dom";
import TopbarUserMessage from './message';
import TopbarUserNotification from './notification';
import TopbarUserProfile from './profile';
import TopbarRightSideBarBtn from './right-sidebar-btn';
import RightSidebar from '../right-sidebar';
import {  Container,Row, Col,Form,Button, Image } from 'react-bootstrap';


class Topbar extends React.Component {

    constructor(props) {
        super(props);
            
        this.state = {
            toggleClass: false,
            showRightSideBar: false,
        };
        // This binding is necessary to make `this` work in the callback
        this.handleToggleClass = this.handleToggleClass.bind(this);
        this.showRightSideBarHandler = this.showRightSideBarHandler.bind(this);
      }

    // nav collapsed handle
    handleToggleClass= (event) =>  {
        event.preventDefault();

        const rootNodeChildren = document.getElementById('root').children;
        for (let i = 0; i < rootNodeChildren.length; i++) 
            if(rootNodeChildren[i].classList.contains('nav-collapsed'))
                rootNodeChildren[i].classList.remove('nav-collapsed')
            else
                rootNodeChildren[i].classList.add('nav-collapsed')
    }

    showRightSideBarHandler(){

        const currentState = this.state.showRightSideBar;
        this.setState({
            showRightSideBar: !currentState,
        });
    }

    render() {

        return (
            <React.Fragment>
            {/* ============================================================== */}
            {/* 						Topbar Start 						   */}
            {/* ============================================================== */}
            <div className="top-bar primary-top-bar">
                <Container fluid>
                    <Row>
                    <Col>
                        <Link className="admin-logo" to="/" >
                            <h1>
                                <Image alt="" src="/assets/img/icon.png" className="logo-icon margin-r-10" />
                                <Image alt="" src="/assets/img/logo-dark.png" className="toggle-none hidden-xs" />
                            </h1>
                        </Link>
                        <div className="left-nav-toggle" onClick={(e) =>this.handleToggleClass(e)}>
                            <Button as="a" variant="link" className="nav-collapse p-0">
                                <i className="fa fa-bars" />
                            </Button>
                        </div>
                        <div className="left-nav-collapsed">
                            <Button as="a" variant="link" className="nav-collapsed p-0" onClick={(e) => this.handleToggleClass(e)}>
                                <i className="fa fa-bars" />
                            </Button>
                        </div>
                        <div className="search-form hidden-xs">
                            <Form>
                                <Form.Control type="search" placeholder="Search for..."/>
                                <Button type="submit" variant="link" className="btn-search">
                                    <i className="fa fa-search"></i>
                                </Button>
                            </Form>
                        </div>
                    </Col>
                    <Col>
                        <ul className="list-inline top-right-nav">
                            <TopbarUserMessage />
                            <TopbarUserNotification />
                            <TopbarRightSideBarBtn showRightSideBarHandler={this.showRightSideBarHandler} />
                            <TopbarUserProfile />
                        </ul>
                    </Col>
                    </Row>
                </Container>
            </div>
            {/* ============================================================== */}
            {/*                        Topbar End                              */}
            {/* ============================================================== */}

            {/* ============================================================== */}
            {/*                   RightSidebar start                           */}
            {/* ============================================================== */}

            <RightSidebar show={this.state.showRightSideBar}   />
         
            {/* ============================================================== */}
            {/*                    RightSidebar End                            */}
            {/* ============================================================== */}
            </React.Fragment>
        );
    }
}

export default Topbar;