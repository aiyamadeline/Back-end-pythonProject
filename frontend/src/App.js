import React, { useState } from 'react';
import SearchForm from './components/searchForm';
import SearchResults from './components/searchResults';
import LoginForm from './components/login';
import RegisterForm from './components/register';
import './App.css';

function App() {
  // State for the search results
  const [results, setResults] = useState([]);

  return (
  <div class = "container">
    <header>
    </header>
    <main>
      <SearchForm onSearch={setResults} />
      <SearchResults results={results} />
      <LoginForm/>
      <RegisterForm/>
      </main>
    <footer>
    </footer>
  </div>
  );
}

export default App;