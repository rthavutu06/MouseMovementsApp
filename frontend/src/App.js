import React, { useState } from 'react';

function App() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  const handleCommandChange = (e) => {
    setCommand(e.target.value);
  };

  const sendCommand = async () => {
    const res = await fetch('http://127.0.0.1:5000/command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ command }),
    });
    const data = await res.json();
    setResponse(data.message);
  };

  return (
    <div className="App">
      <h1>Run Commands</h1>
      <input
        type="text"
        value={command}
        onChange={handleCommandChange}
        placeholder="Enter command"
      />
      <button onClick={sendCommand}>Send Command</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
