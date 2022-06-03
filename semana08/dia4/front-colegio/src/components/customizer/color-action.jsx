import React from 'react';
import { Row, Col } from 'react-bootstrap';

const ColorAction = () => {

    const type = [
        {
            name: 'Userbox'
        },
        {
            name: 'Page Header'
        },
        {
            name: 'Navigation'
        },
        {
            name: 'Header'
        },
        {
            name: 'Sidebar'
        }
    ];

    const colorCode = [
        {
            name: 'color_1',
            primary: "#ffff",
            secondary: "#0000"
        },
        {
            name: 'color_2',
            primary: "#143b64",
            secondary: "#0000"
        },
        {
            name: 'color_3',
            primary: "#7356f1",
            secondary: "#0000"
        },
        {
            name: 'color_4',
            primary: "#4527a0",
            secondary: "#0000"
        },
        {
            name: 'color_5',
            primary: "#c62828",
            secondary: "#0000"
        },
        {
            name: 'color_6',
            primary: "#283593",
            secondary: "#0000"
        },
        {
            name: 'color_7',
            primary: "#1e78ff",
            secondary: "#0000"
        },
        {
            name: 'color_8',
            primary: "#3695eb",
            secondary: "#0000"
        },
        {
            name: 'color_9',
            primary: "#00838f",
            secondary: "#0000"
        },
        {
            name: 'color_10',
            primary: "#ff8f16",
            secondary: "#0000"
        },
        {
            name: 'color_11',
            primary: "#6673fd",
            secondary: "#0000"
        },
        {
            name: 'color_12',
            primary: "#558b2f",
            secondary: "#0000"
        },
        {
            name: 'color_13',
            primary: "#2a2a2a",
            secondary: "#0000"
        },
        {
            name: 'color_14',
            primary: "#1367c8",
            secondary: "#0000"
        },
        {
            name: 'color_15',
            primary: "#ed0b4c",
            secondary: "#0000"
        }
    ];
    return (
        <Row className="color-action">
            {type.map((item, key) => {
                return (
                    <Col sm="12" className="mb-2" key={key}>
                        <h6>{item.name}</h6>
                        <div className="box d-flex align-content-start flex-wrap">
                        {colorCode.map((color, k) => {
                            return (
                                <span className="list" 
                                    data-name={color.name} 
                                    primary-color={color.primary} 
                                    secondary-color={color.secondary} key={k}
                                    style={{backgroundColor: color.primary, outline: `1px solid `+color.secondary}}
                                >
                                    <div></div>
                                </span>
                            );
                        })} 
                        </div>
                    </Col>
                );
            })} 
        </Row>
    );
}

export default ColorAction;