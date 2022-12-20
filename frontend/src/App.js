import React, { useState } from 'react';
import SearchForm from '../SearchForm';
import SearchResults from '../SearchResults';

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