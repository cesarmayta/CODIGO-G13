import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';

import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';

import Layout from './layouts'

import * as serviceWorker from './serviceWorker';

import Alumnos from './pages/alumnos';

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter basename={'/'} >
      <Switch>
        

          <Layout name="backend">
            <Route path={`/alumnos`} component={Alumnos} />
          </Layout>
      </Switch>
    </BrowserRouter>
    <ToastContainer />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
