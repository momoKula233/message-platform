import React from 'react';
import { Form, Select, Input, Button, Upload, Icon } from 'antd';
import http from '../services';
const Option = Select.Option;





class App extends React.Component {
  config = {
    name: 'file',
    action: 'http://127.0.0.1:5000/upload',
  };
  onChange = (info) => {
    if(info.file.response) {
      this.image = info.file.response;
    }
  }
  handleSubmit = (e) => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        http.post('/register', {
          display_name: values['username'],
          password: values['password'],
          gender: values['gender'],
          age: values['age'],
          avatar: this.image,
        })
      }
    });
  }
  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <Form onSubmit={this.handleSubmit} style={{ paddingTop: '30px' }}>
        <Form.Item
          label="username"
          labelCol={{ span: 4 }}
          wrapperCol={{ span: 8 }}
        >
          {getFieldDecorator('username', {
            rules: [{ required: true, message: 'Please input your username!' }],
          })(
            <Input placeholder="username" />
          )}
        </Form.Item>
        <Form.Item
          label="password"
          labelCol={{ span: 4 }}
          wrapperCol={{ span: 8 }}
        >
          {getFieldDecorator('password', {
            rules: [{ required: true, message: 'Please input your password!' }],
          })(
            <Input type='password' placeholder="password" />
          )}
        </Form.Item>
        <Form.Item
          label="age"
          labelCol={{ span: 4 }}
          wrapperCol={{ span: 8 }}
        >
          {getFieldDecorator('age', {
            rules: [{ required: false, message: 'Please input your age!' }],
          })(
            <Input type='number' placeholder="age" />
          )}
        </Form.Item>
        <Form.Item
          label="Gender"
          labelCol={{ span: 4 }}
          wrapperCol={{ span: 8 }}
        >
          {getFieldDecorator('gender', {
            rules: [{ required: true, message: 'Please select your gender!' }],
          })(
            <Select
              placeholder="Select your gender"
            >
              <Option value="male">male</Option>
              <Option value="female">female</Option>
            </Select>
          )}
        </Form.Item>
        <Form.Item wrapperCol={{ span: 8, offset: 4 }} >
          <Upload {...this.config} onChange={this.onChange}>
              <Button>
                <Icon type="upload" /> Click to Upload
              </Button>
            </Upload>          
        </Form.Item>
        <Form.Item
          wrapperCol={{ span: 8, offset: 4 }}
        >
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    );
  }
}

const WrappedApp = Form.create()(App);

export default WrappedApp;