import React from 'react';
import { Row, Col, Form } from 'react-bootstrap';



//     Container:[
//         {value: "wide",label: 'wide'},
//         {value: "boxed",label: 'boxed'},
//         {value: "wide-boxed",label: 'Wide Boxed'}
//     ]
    


    
// }

const BackgroundType = () => (

    <Col sm="12">
        <h6 className="title">Background</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>Light</option>
                <option>Dark</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)



const LayoutType = () => (

    <Col sm="12">
        <h6 className="title">Layout</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>Vertical</option>
                <option>Horizontal</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)


const SideBarType = () => (

    <Col sm="12">
        <h6 className="title">Sidebar</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>Full</option>
                <option>Mini</option>
                <option>Compact</option>
                <option>Modern</option>
                <option>Overlay</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)

const SidebarPosition = () => (

    <Col sm="12">
        <h6 className="title">Sidebar Position</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>Static</option>
                <option>Fixed</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)

const HeaderPosition = () => (

    <Col sm="12">
        <h6 className="title">Header Position</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>Static</option>
                <option>Fixed</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)

const Container = () => (

    <Col sm="12">
        <h6 className="title">Container</h6>
        <div className="">
            <Form.Group controlId="exampleForm.SelectCustom">
                <Form.Label>Custom select</Form.Label>
                <Form.Control as="select" custom>
                <option>wide</option>
                <option>Boxed</option>
                </Form.Control>
            </Form.Group>
        </div>
    </Col>
  
)



const LayoutAction = () => {

    return (
        <Row className="layout-action">
            
            <BackgroundType/>
            <LayoutType/>
            <SideBarType/>
            <SidebarPosition/>
            <HeaderPosition/>
            <Container/>
        </Row>
    );
}

export default LayoutAction;