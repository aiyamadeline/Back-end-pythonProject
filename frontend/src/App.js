import React, { useState } from 'react';
import SearchForm from './components/searchForm';
import SearchResults from './components/searchResults';

function App() {
  // State for the search results
  const [results, setResults] = useState([]);

  return (
    <div>
      <SearchForm onSearch={setResults} />
      <SearchResults results={results} />
    </div>
  );
}

export default App;