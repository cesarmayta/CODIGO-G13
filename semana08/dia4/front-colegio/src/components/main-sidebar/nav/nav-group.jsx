import React from 'react';
import BeNavItem from './nav-item';

export default function BeNavGroup(props)  {

    return (
        <React.Fragment>
            {props.menu.map((item, key) => {
                return (
                    <React.Fragment>
                        <BeNavItem nav={item} key={key} rootNav={true} /> 
                    </React.Fragment>
                );
            })} 
        </React.Fragment>
    );

}

