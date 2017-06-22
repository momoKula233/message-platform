import React from 'react';
import ReactDOM from 'react-dom';
import App from './route';
import registerServiceWorker from './registerServiceWorker';
import './styles/index.less';


ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
