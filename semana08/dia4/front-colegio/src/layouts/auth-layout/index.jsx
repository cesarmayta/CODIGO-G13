import React from 'react'
import {Helmet} from "react-helmet";
import { Row, Container, Col, Image } from 'react-bootstrap';

export default function AuthLayout (props) {

    return (
        <React.Fragment>
            
            <Helmet>
                <title> FixedPlus - Bootstrap Admin Dashboard Template </title>
            </Helmet>

            <div className="misc-wrapper">
                <div className="misc-content">
                    <Container>
                    <Row  className="justify-content-center">
                        <Col sm="12" md="5" lg="4"  className="col-4">
                        <div className="misc-header text-center">
                            <Image alt="" src="/assets/img/icon.png" className="logo-icon margin-r-10" />
                            <Image alt="" src="/assets/img/logo-dark.png" className="toggle-none hidden-xs" />
                        </div>
                        <div className="misc-box">   
                            { props.children }
                        </div>
                        <div className="text-center misc-footer">
                            <p>Copyright © 2020 Ducor</p>
                        </div>
                        </Col>
                    </Row>
                    </Container>
                </div>
            </div>
        </React.Fragment>
    )

}

