import React from 'react';
import { Form, Input, Button } from 'antd';
import http from '../services';

class App extends React.Component {
  handleSubmit = async(e) => {
    e.preventDefault();
    this.props.form.validateFields(async(err, values) => {
      if (!err) {
        const {data} = await http.post('/login', {
          display_name: values['username'],
          password: values['password'],
        })
        if(data.success) {
          localStorage.setItem('TOKEN', JSON.stringify(data))
        }
      }
    });
  }
  handleSelectChange = (value) => {
    console.log(value);
  }
  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <div className="form">
        <Form onSubmit={this.handleSubmit} style={{ paddingTop: '30px', width: '500px' }}>
          <Form.Item
            label="user"
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 12 }}
          >
            {getFieldDecorator('username', {
              rules: [{ required: true, message: 'Please input your username!' }],
            })(
              <Input placeholder="username" />
            )}
          </Form.Item>
          <Form.Item
            label="password"
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 12 }}
          >
            {getFieldDecorator('password', {
              rules: [{ required: true, message: 'Please input your password!' }],
            })(
              <Input type='password' placeholder="password" />
            )}
          </Form.Item>
          <Form.Item
            wrapperCol={{ span: 12, offset: 8 }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

const WrappedApp = Form.create()(App);

export default WrappedApp;