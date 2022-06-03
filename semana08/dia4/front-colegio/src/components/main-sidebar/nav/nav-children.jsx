import React from 'react';
import BeNavItem from './nav-item';

export default function BeNavChildren  ({children}) {
    
    const menu =  children;

    if(menu){
        return (
            <React.Fragment>
                {menu.map((item, key) => {
                    return <BeNavItem nav={item} key={ key } />
                })} 
            </React.Fragment>
        );
    }else{
        return;
    }

}

