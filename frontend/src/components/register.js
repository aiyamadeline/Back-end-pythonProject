import React, { useState } from 'react';
import axios from 'axios';
function RegisterForm() {
  const [showForm, setShowForm] = useState(false);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleSubmit = (event) => {
    event.preventDefault();
    // Send request to server to register the user
    axios.post('/register', { username, email, password })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  return (
    <div>
      <button id = "registerButton" onClick={() => setShowForm(true)}>Register</button>
      <form className = "Register" style={{ display: showForm ? 'block' : 'none' }} onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="username" value={username} onChange={(event) => setUsername(event.target.value)} />
        </label>
        <label>
          Email:
          <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
export default RegisterForm;