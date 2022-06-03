import React from 'react';

class RightSidebar extends React.Component {

    
    render() {
        
        return (
            <React.Fragment>
            {/* ============================================================== */}
            {/*                        Right Side Start                        */}
            {/* ============================================================== */}
            <nav className={this.props.show? "toggle-sidebar right-sidebar-toggle": "toggle-sidebar"}>
            <div className="nano">
                <div className="nano-content">
                <div>
                    <ul className="list-inline nav-tab-card clearfix" role="tablist">
                    <li className="active" role="presentation">
                        <a aria-controls="friends" data-toggle="tab" href="#friends" role="tab">Friends</a>
                    </li>
                    </ul>
                    <div className="tab-content">
                    <div className="tab-pane active" id="friends">
                        <ul className="list-unstyled sidebar-contact-list">
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-2.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>John Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-1.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Govinda Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-danger circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-3.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Megan Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-4.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Hritik Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-5.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Bianca Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-6.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>John Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-success circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-1.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Govinda Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li className="clearfix">
                            <a className="media-box" href="#be"><span className="float-right"><span className="circle circle-danger circle-lg" /></span> <span className="float-left">
                                <img alt="user" className="media-box-object rounded-circle" src="/assets/img/avtar-2.png" width={50} /></span>
                            <span className="media-box-body"><span className="media-box-heading"><strong>Megan Doe</strong><br />
                                <small className="text-muted">Designer</small></span></span></a>
                        </li>
                        <li>
                            <div className=" text-center">
                            <a className="btn btn-teal" href="#be" title="See more contacts">Load more..</a>
                            </div>
                        </li>
                        </ul>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </nav>
            {/* ============================================================== */}
            {/*                        Right Side End                          */}
            {/* ============================================================== */}

            </React.Fragment>
        );
    }
}

export default RightSidebar;