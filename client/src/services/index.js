import axios from 'axios';

const client = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
});

client.interceptors.request.use(conf => {
  let token = localStorage.getItem('TOKEN');
  token = JSON.parse(token);
  if(token) conf.headers.authorization = `Bearer ${token['access_token']}`;
  return conf;
});

export default client;