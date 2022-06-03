import React from 'react'
import { Breadcrumb, Col } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './style.scss';

const PageHeader = ()  => {

    let last_path = "";
    if(window.location.pathname){
       last_path = window.location.pathname.split('/');
       last_path = last_path[last_path.length-1];
    }

    return (
        <div className="page-header">
            <Col lg="6" className="align-self-center ">
                <h2>{ last_path }</h2>
                <Breadcrumb>
                    <Breadcrumb.Item>
                        <Link to={`/`}>Home</Link>
                    </Breadcrumb.Item>
                    <Breadcrumb.Item>
                        {last_path}
                    </Breadcrumb.Item>
                </Breadcrumb>
            </Col>
        </div>
    )
}

export default PageHeader