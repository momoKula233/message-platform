import axios from 'axios';

const client = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
});

client.interceptors.request.use(conf => {
  const token = localStorage.getItem('TOKEN');
  if(token) conf.headers.authorization = `Bearer ${token}`;
  return conf;
});

export default client;