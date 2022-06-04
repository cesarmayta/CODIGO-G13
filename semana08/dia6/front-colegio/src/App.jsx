import Main from './pages/Main';
import AuthService from './services/auth.service';
import {createBrowserHistory} from 'history';
import  {useEffect} from 'react';

function App() {

  useEffect(() => {
    const token = AuthService.getToken();

    if(!token){
        const history = createBrowserHistory();
        history.push('/');
        window.location.reload();
    }
  });
  return (
    <Main/>
  )
}

export default App
