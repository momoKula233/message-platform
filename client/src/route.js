import React from 'react';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import 'normalize-css';
import { Layout } from 'antd';
import Login from './views/Login';
import Register from './views/Register';
import Home from './views/Home';
const { Header, Footer, Sider, Content } = Layout;

const routes = [
  { path: '/login', component: Login, name: 'login' },
  { path: '/register', component: Register, name: 'register' },
  { path: '/home', component: Home, name: 'home' },
]

export default class Router extends React.PureComponent {
  render() {
    return (<BrowserRouter>
    <Layout>
      <Switch>
        { routes.map((route, index) => {
          return <Route key={`${index}`} render={()=> <div>
            <Header className='page-header'>{route.name}</Header>
            <Content>
              <route.component />
            </Content>
          </div>}></Route>
        }) }
      </Switch>
    </Layout>
  </BrowserRouter>)
  }
}