import React from 'react';
import UserStore from '../store';

const userStore = new UserStore();

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    if(!userStore.isLoggedIn) window.location.href = '/login';
  }
  render() {
    if(!userStore.isLoggedIn) return null;
    return <div>
      home
    </div>
  }
}