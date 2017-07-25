import React from 'react';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import 'normalize-css';
import {Layout, Menu, Modal} from 'antd';
import Login from './views/Login';
import Register from './views/Register';
import Home from './views/Home';
import User from './views/UserIndex';
import UserStore from './store/';
import { Provider } from 'mobx-react';

const {Header, Content, Sider} = Layout;

const routes = [
  {path: '/login', component: Login, name: 'login'},
  {path: '/register', component: Register, name: 'register'},
  {path: '/home', component: Home, name: 'home', sider: true},
  {path: '/user', component: User, name: 'user', sider: true},
];

export default class Router extends React.PureComponent {
  userStore = new UserStore();
  render() {
    return (
    <Provider user={this.userStore}>
    <BrowserRouter>
      <Layout>
        <Switch>
          {routes.map((route, index) => {
            return <Route key={`${index}`} path={route.path} render={(props) => {
              return (<div>
                <Header className='page-header'>{route.name}</Header>
                <Content className="page-content">
                  {route.sider && <Sider className="slide-menu">
                    <Menu mode="inline" defaultSelectedKeys={['home']} theme="light"
                          onClick={(item) => console.log(item)}>
                      <Menu.Item key="home">home</Menu.Item>
                      <Menu.Item key="user">user index</Menu.Item>
                    </Menu>
                  </Sider>}
                  <section className="page-info">
                    <route.component {...props} />
                  </section>
                </Content>
              </div>)
            }
            }></Route>
          })}
        </Switch>
      </Layout>
    </BrowserRouter>
    </Provider>)
  }
}