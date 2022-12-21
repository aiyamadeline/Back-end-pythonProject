import React, { useState } from 'react';

const SearchForm = () => {
  // State for the search query
  const [query, setQuery] = useState('');

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();

    // Send a GET request to the API endpoint from the Python backend, passing the search query as a query parameter (`/api/search?q=)
    
    fetch(`http://localhost:5000/${query}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the API and display the search results to the user
        console.log(data);
      });
  };

  return (
   // <form onSubmit={handleSubmit}>
   <form action='http://localhost:5000/' method='POST'>
      <input
        name='query'
        type="text"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchForm;
