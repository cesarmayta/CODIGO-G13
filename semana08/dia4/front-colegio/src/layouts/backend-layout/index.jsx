import React from 'react'

import {Helmet} from "react-helmet";
import Topbar from '../../components/topbar';
import MainSidebar from '../../components/main-sidebar';
import Footer from '../../components/footer';
import PageHeader from '../../components/page-header';
// import Customizer from '../../customizer';

export default function BackendLayout ({children}) {

    return (
        <React.Fragment>
            
            <Helmet>
                <title>FixedPlus - Bootstrap Admin Dashboard Template</title>
                <style>
                </style>
            </Helmet>
            <Topbar />
            <MainSidebar />

            <PageHeader />
            <div className="main-content">
                {children}
                <Footer />
            </div>
            {/* <Customizer />  */}
        </React.Fragment>
    )
}

