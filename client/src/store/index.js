import {observable, computed} from 'mobx';

export default class UserStore {
  @observable user = { current: JSON.parse(localStorage.getItem('TOKEN')).user };
  @computed get isLoggedIn() {
    const user = JSON.parse(localStorage.getItem('TOKEN'));
    return !!user
  }
  update(user) {
    this.user.current = user;
  }
  login(data) {
    localStorage.setItem('TOKEN', data);
  }
  logout() {
    this.user.current = null;
    localStorage.clear();
  }
}