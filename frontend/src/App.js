import React, { useState } from 'react';

function SearchForm() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    fetch(`http://localhost:5000/search?query=${query}`)
      .then((response) => response.json())
      .then((data) => {
        setResults(data.results);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <button type="submit">Search</button>
      <SearchResults results={results} />
    </form>
  );
}

function SearchResults({ results }) {
  return (
    <ul>
      {results.map((result) => (
        <li key={result.id}>{result.title}</li>
      ))}
    </ul>
  );
}

export default SearchForm;







