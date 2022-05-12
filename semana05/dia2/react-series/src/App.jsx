import React,{Component} from 'react';
import axios from 'axios';

class App extends Component{
  constructor(props){
    super(props);
    this.state = ({
      series:[],
      pos:null,
      titulo:'Nuevo',
      id:0,
      nombre:'',
      fecha:'',
      rating:'0',
      categoria:''
    })
  }

  componentDidMount(){
    axios.get('http://localhost:8000/api/series/')
    .then(res =>{
      console.log(res.data)
    })
  }

  render(){
    return(
      <div>Series</div>
    )
  }
}

export default App;

