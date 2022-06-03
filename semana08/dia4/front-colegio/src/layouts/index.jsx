import React from 'react'
import BackendLayout from './backend-layout';
import AuthLayout from './auth-layout';

export default function Layout (props){

    let layout = 'backend';

    if( layout === 'auth' )
        return (<AuthLayout name={layout}>{ props.children }</AuthLayout>)

    else if( layout === 'backend' )
        return ( <BackendLayout name={layout}>{ props.children }</BackendLayout>)

    else
        return (<BackendLayout name={layout}>{ props.children }</BackendLayout>)

}

