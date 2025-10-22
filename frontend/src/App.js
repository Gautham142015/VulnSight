import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [vulnerabilities, setVulnerabilities] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleScan = async () => {
    setLoading(true);
    try {
      const response = await axios.post('/scan', { url });
      setVulnerabilities(response.data.vulnerabilities);
    } catch (error) {
      console.error('Error scanning:', error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>VulnSight</h1>
        <p>A Web Vulnerability Scanner</p>
      </header>
      <main>
        <div className="scan-form">
          <input
            type="text"
            placeholder="Enter URL to scan"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button onClick={handleScan} disabled={loading}>
            {loading ? 'Scanning...' : 'Scan'}
          </button>
        </div>
        <div className="results">
          <h2>Scan Results</h2>
          {vulnerabilities.length === 0 ? (
            <p>No vulnerabilities found yet. Start a scan to see results.</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Type</th>
                  <th>URL</th>
                  <th>Payload</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                {vulnerabilities.map((vuln, index) => (
                  <tr key={index}>
                    <td>{vuln.type}</td>
                    <td>{vuln.url}</td>
                    <td>{vuln.payload}</td>
                    <td>{vuln.description}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
