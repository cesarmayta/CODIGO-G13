import React from 'react';
import { Link } from "react-router-dom";

const TopbarRightSideBarBtn = (props) => {

    return (
        <li className="dropdown d-none-m">
            <Link className="right-sidebar-toggle"  
                onClick={ () => props.showRightSideBarHandler()  }
            >
                <i className="fa fa-align-right" />
            </Link>
        </li>
    );
}

export default TopbarRightSideBarBtn;