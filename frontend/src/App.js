import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({ name: '', address: '', template_id: '1' });
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = new FormData();
    data.append('name', formData.name);
    data.append('address', formData.address);
    data.append('template_id', formData.template_id);
    data.append('image', image);

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/generate/', data);
      setResult(response.data.card_url);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold text-center mb-10">Eid Card Generator</h1>
      <form onSubmit={handleSubmit} className="max-w-lg mx-auto bg-white p-6 rounded-lg shadow">
        <input type="text" placeholder="Full Name" className="w-full mb-4 p-2 border" onChange={e => setFormData({...formData, name: e.target.value})} required />
        <input type="text" placeholder="Address" className="w-full mb-4 p-2 border" onChange={e => setFormData({...formData, address: e.target.value})} required />
        <select className="w-full mb-4 p-2 border" onChange={e => setFormData({...formData, template_id: e.target.value})}>
          <option value="1">Deep Green - Royal</option>
          <option value="2">Minimalist Blue</option>
        </select>
        <input type="file" className="w-full mb-4" onChange={e => setImage(e.target.files[0])} required />
        <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded">{loading ? 'Processing...' : 'Generate Card'}</button>
      </form>

      {result && (
        <div className="mt-10 text-center">
          <img src={result} alt="Eid Card" className="mx-auto shadow-lg max-w-sm" />
          <a href={result} download className="inline-block mt-4 bg-green-600 text-white px-6 py-2 rounded">Download High Quality</a>
        </div>
      )}
    </div>
  );
}

export default App;
