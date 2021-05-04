import {useState} from "react";
import useLocalStorage from 'react-use-localstorage'
import {BrowserRouter as Router, Route, Switch} from "react-router-dom"

import ChatApp from "./Chatapp/App";
import LoginApp from "./Login/App";


export default function App() {
    const [jwt, setJwt] = useState(Object)
    const [accessToken, setAccessToken] = useLocalStorage('a_key')
    const [refreshToken, setRefreshToken] = useLocalStorage('r_key')
    if (Object.keys(jwt).length === 0 && accessToken && refreshToken) {
        const data = {"refresh": refreshToken, 'access': accessToken}
        setJwt(data)
    } else if (Object.keys(jwt).length !== 0 && !accessToken && !refreshToken) {
        setAccessToken(jwt.access)
        setRefreshToken(jwt.refresh)
    }


    return (
        <Router>
            <Switch>
                <Route path='/chat/' exact
                       component={() => <ChatApp/>}/>
                <Route path='/login/' exact component={() => <LoginApp setJwt={setJwt}/>}/>
            </Switch>
        </Router>
    )
}

