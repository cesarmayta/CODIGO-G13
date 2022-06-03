import React from 'react';
import { Link } from 'react-router-dom';
import BeNavChildren from './nav-children';
import { Nav } from 'react-bootstrap'


class  BeNavItem  extends React.Component   {
    
    constructor(props) {
        super(props);
        this.state={
            childClick: false
        }

        this.handleToggle = this.handleToggle.bind(this);
    }

    handleToggle(event, childStatus, uuid){

        if(!childStatus){
            return false
        }


        const navItem = event.currentTarget.parentNode;
        const navChild = event.currentTarget.nextSibling;

        // remove .active class for #menu area
        // id #menu
        const menuNode = event.currentTarget.parentNode.parentNode.childNodes;

        for (let i = 0; i < menuNode.length; i++) {
            // check menu uuid
            if( menuNode[i].firstChild.attributes.getNamedItem('menu-uuid')?? false )
               // console.log( menuNode[i].firstChild.attributes.getNamedItem('menu-uuid').value );
               if( menuNode[i].firstChild.attributes.getNamedItem('menu-uuid').value === uuid)
                   continue;

                
            if(menuNode[i].classList.contains('active')){

                // change child class name element name ul
                menuNode[i].lastChild.classList.remove('in');
                menuNode[i].classList.remove('active');


            }
        }


// ===========================================================


        if(navItem.classList.contains('active')){

            // change parent class name
            navItem.classList.remove('active');
            // change child class name element name ul
            navChild.classList.remove('in');
           

        } else { 

            // change child class name element name ul
            navItem.classList.add('active');
            navChild.classList.add('in')
       
        }

        event.preventDefault();

    }

    render() {
        const nav = this.props.nav;

        let rootNav = false;
        if(this.props.rootNav){
            rootNav = true;
        }

        if(!nav) return;

            return (
                <Nav.Item as='li'
                //    onMouseEnter={ () => this.mouseEnter }
                >
                    <Link className="nav-link" 
                        to={ nav.to? nav.to: "#be" } 
                        key={nav.uuid}
                        menu-uuid={nav.uuid}
                        onClick={ (e, childStatus, uuid) => this.handleToggle(e, childStatus = nav.children?1:0, uuid = nav.uuid) }
                    >
                     

                    {/* icon  */}
                     {(() => {
                        if ( nav.icon ){
                            return (
                                <i className={ nav.icon }></i>
                            )
                        }
                    })()}
            
                    
                    {(() => {
                    if ( nav.children ){
                        return (
                            <span className="toggle-none">
                                { nav.name }
                                <span className="fa arrow " /> 
                            </span>
                        )
                    }
                    else if(rootNav){
                        return (
                            <span className="toggle-none">
                            { nav.name }
                            </span>
                        );
                    }
                    else{
                        return (
                            <React.Fragment>
                            { nav.name }
                            </React.Fragment>
                        );
                    }
                    })()}
                        
                    </Link>

                    {(() => {
                    if ( nav.children ){
                        return (
                            <Nav as='ul' className="nav-second-level flex-column sub-menu collapse">
                                <BeNavChildren children={nav.children} />
                            </Nav>
                        )
                    }
                    })()}

                </Nav.Item>
            );
        }
    }



export default BeNavItem;

