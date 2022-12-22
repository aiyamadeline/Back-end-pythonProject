import React, { useState } from 'react';
import SearchForm from './components/searchForm';
import SearchResults from './components/searchResults';
import LoginForm from './components/login';

function App() {
  // State for the search results
  const [results, setResults] = useState([]);

  return (
    <div>
      <SearchForm onSearch={setResults} />
      <SearchResults results={results} />
      <LoginForm/>
    </div>
  );
}

export default App;