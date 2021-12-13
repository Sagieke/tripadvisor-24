import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import logo from './logo.svg';
import AddPlace from "./components/AddPlace";
import MainPage from "./components/MainPage";
import UserPage from "./components/UserPage";
import LogOut from "./components/LogOut";

import "./App.css";
import Logo from "./components/Logo";
import Admin from "./components/Admin";


function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
        <Link className="navbar-brand" to={"/"}> <img src={logo} className="App-logo" alt="logo" /></Link>
        <Switch>
        <Route exact path="/MainPage" component ={MainPage}/>
        <Route exact path="/UserPage" component ={LogOut}/>
        </Switch>
          </div>
        </nav>
        <Switch>
              <Route exact path="/Admin" component ={Admin}/> 
              <Route exact path="/MainPage" component ={Logo}/>
              <Route exact path="/userPage" component={UserPage}/>
            </Switch>
      </div>
      <footer>
        <AddPlace/>
      </footer>
    </Router>
    
  );
}

export default App;
