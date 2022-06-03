import React from 'react';

export class DefaultConfig {
  static data = {

        // settngs: {
        //     direction:  'ltr',
        //     background: 'light',
        //     body_type: 'default',
        //     sidebar_setting: 'default-sidebar', 
        //     sidebar_background_setting: '',
        // },
       
       color: {
           userbox: {
                primary: "#ffff",
                secondary: "#0000"
           },
           pageHeader: {
                primary: "#ffff",
                secondary: "#0000"
           },
           navigation: {
                primary: "#ffff",
                secondary: "#0000"
           },
           sidebar: {
                primary: "#ffff",
                secondary: "#0000"
           }
       },
   }
 }

const UserConfig = () => {
  
    return (
        <React.Fragment>

        </React.Fragment>
    )
  
 }


 export const get = () => {

 }

  export const find = key => {

 }


  export const set = (key, value) => {
     
 }


export default UserConfig;