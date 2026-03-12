import React, { useState } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

function App() {
  const [formData, setFormData] = useState({ name: '', address: '', template_id: '1' });
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');

  const handleImage = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = new FormData();
    data.append('name', formData.name);
    data.append('address', formData.address);
    data.append('template_id', formData.template_id);
    data.append('image', image);

    try {
      const response = await axios.post(`${API_URL}/api/generate/`, data);
      setResult(response.data.card_url);
    } catch (err) {
      alert("Error generating card");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-5 md:p-10">
      <h1 className="text-4xl font-bold text-center mb-10 text-green-900">Eid Card Generator 2026</h1>
      
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10">
        <div className="bg-white p-8 rounded-2xl shadow-xl">
          <form onSubmit={handleSubmit} className="space-y-6">
            <input type="text" placeholder="Full Name" className="w-full p-4 border rounded-lg focus:ring-2 focus:ring-green-500" onChange={e => setFormData({...formData, name: e.target.value})} required />
            <input type="text" placeholder="Address" className="w-full p-4 border rounded-lg focus:ring-2 focus:ring-green-500" onChange={e => setFormData({...formData, address: e.target.value})} required />
            
            <div className="grid grid-cols-4 gap-2 h-48 overflow-y-auto border p-4 rounded-lg bg-gray-50">
              {[...Array(20)].map((_, i) => (
                <button 
                  key={i} type="button"
                  onClick={() => setFormData({...formData, template_id: (i+1).toString()})}
                  className={`p-2 text-xs font-bold rounded border ${formData.template_id === (i+1).toString() ? 'bg-green-600 text-white border-green-700' : 'bg-white text-gray-700'}`}
                >
                  Style {i + 1}
                </button>
              ))}
            </div>

            <div className="flex items-center space-x-4">
              <input type="file" className="text-sm" onChange={handleImage} required />
              {preview && <img src={preview} className="w-16 h-16 rounded-full object-cover border-2 border-green-500" alt="Avatar" />}
            </div>

            <button type="submit" className="w-full bg-green-700 hover:bg-green-800 text-white font-bold py-4 rounded-xl shadow-lg transition duration-300" disabled={loading}>
              {loading ? 'Processing...' : 'Generate High Resolution Card'}
            </button>
          </form>
        </div>

        <div className="bg-white p-8 rounded-2xl shadow-xl flex flex-col items-center justify-center min-h-[500px]">
          {result ? (
            <div className="text-center">
              <img src={result} alt="Eid Card" className="rounded-lg shadow-2xl mb-6 border-4 border-gray-100 max-w-full h-auto" />
              <div className="flex space-x-4 justify-center">
                <a href={result} download className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-bold">Download JPG</a>
                <button onClick={() => window.open(`https://wa.me/?text=Eid Mubarak! Check my card: ${result}`)} className="bg-green-500 hover:bg-green-600 text-white px-8 py-3 rounded-lg font-bold">Share</button>
              </div>
            </div>
          ) : (
            <div className="text-gray-400 text-center">
              <p className="text-6xl mb-4">🌙</p>
              <p className="italic">Fill the form and select a style to generate your card</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
