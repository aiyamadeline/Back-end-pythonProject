import React from 'react';
import Axios from 'axios';

class LoginForm extends React.Component {
  handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get('username');
    const password = formData.get('password');
    Axios.post('/login', {
      username: username,
      password: password,
    })
      .then((response) => {
        // Handle successful login
      })
      .catch((error) => {
        // Handle failed login
      });
  };
  render() {
    return (
      <form className= "Login" onSubmit={this.handleSubmit}>
        <label id = "username">
          Username:
          <input type="text" name="username" />
        </label>
        <br />
        <label id = "password">
          Password:
          <input type="password" name="password" />
        </label>
        <br />
        <button id = "login" type="submit">Login</button>
      </form>
    );
  }
}
export default LoginForm;