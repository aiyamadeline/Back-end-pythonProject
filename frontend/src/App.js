import React, { useState } from 'react';
import SearchForm from './components/searchForm';
import SearchResults from './components/searchResults';
import LoginForm from './components/login';
import RegisterForm from './components/register';

import './App.css';


function App() {
  // State for the search results
  const [results, setResults] = useState([]);
  
  // State to toggle the register form button

  state = {
    showRegisterForm: false,
  };

  toggleRegisterForm = () => {
    this.setState((prevState) => ({
      showRegisterForm: !prevState.showRegisterForm,
    }));
  };

  return (

  <div class = "container">
    <header>
    </header>
    

      <SearchForm onSearch={setResults} />
      <SearchResults results={results} />
      <LoginForm/>
      

      <button onClick={this.toggleRegisterForm}>
          {this.state.showRegisterForm ? 'Hide' : 'Show'} Register Form
        </button>
        {this.state.showRegisterForm && <RegisterForm />}
    </div>
  );
}

export default App;