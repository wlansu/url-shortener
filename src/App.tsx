import React, { useState, FormEvent } from 'react';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState<string>('');
  const [shortUrl, setShortUrl] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError(''); // Clear previous error
    try {
      const response = await axios.post('http://0.0.0.0:8000/api/shortener/create', { original_url: url });
      setShortUrl(response.data.short_code);
    } catch (err) {
      setError('Failed to shorten the URL. Please try again.');
    }
  };

  return (
    <div>
      <h1>URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL"
          required
        />
        <button type="submit">Shorten</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {shortUrl && (
        <div>
          <p>Short URL: <a href={`http://0.0.0.0:8000/api/shortener/${shortUrl}`}>{window.location.origin}/{shortUrl}</a></p>
        </div>
      )}
    </div>
  );
}

export default App;