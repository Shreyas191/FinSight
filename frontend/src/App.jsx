// REPLACE THIS ENTIRE SECTION IN App.jsx

import React, { useState } from 'react';
import { styles, globalStyles } from './styles/styles';
import Header from './components/Header';
import UploadCard from './components/UploadCard';
import SentimentCard from './components/SentimentCard';
import MetricsCard from './components/MetricsCard';
import ChatInterface from './components/ChatInterface';
import DocumentLibrary from './components/DocumentLibrary';

export default function App() {
  const [file, setFile] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [processed, setProcessed] = useState(false);
  const [query, setQuery] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState(null);
  const [sentiment, setSentiment] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [activeTab, setActiveTab] = useState('upload');
  const [currentDocId, setCurrentDocId] = useState(null);

  // REAL API CALL - Upload File
  const handleFileUpload = async (e) => {
    const uploadedFile = e.target.files[0];
    if (!uploadedFile || uploadedFile.type !== 'application/pdf') {
      alert('Please upload a PDF file');
      return;
    }

    setFile(uploadedFile);
    setProcessing(true);

    const formData = new FormData();
    formData.append('file', uploadedFile);

    try {
      const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Upload failed');
      }

      const data = await response.json();
      
      setCurrentDocId(data.document_id);
      setSummary(data.summary);
      setSentiment(data.sentiment);
      setProcessed(true);
      
      setDocuments(prev => [...prev, {
        id: data.document_id,
        filename: uploadedFile.name,
        uploadDate: new Date().toISOString(),
        sentiment: data.sentiment,
        summary: data.summary
      }]);

      console.log('Upload successful:', data);
    } catch (error) {
      console.error('Upload error:', error);
      alert('Failed to upload PDF. Make sure backend is running on port 8000.');
    } finally {
      setProcessing(false);
    }
  };

  // REAL API CALL - Query Document
  const handleQuery = async () => {
    if (!query.trim() || !processed) return;

    setLoading(true);
    setChatHistory(prev => [...prev, { type: 'user', text: query }]);

    try {
      const response = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: query,
          top_k: 5,
          document_ids: currentDocId ? [currentDocId] : null
        })
      });

      if (!response.ok) {
        throw new Error('Query failed');
      }

      const data = await response.json();
      
      setChatHistory(prev => [...prev, {
        type: 'ai',
        text: data.answer
      }]);

      console.log('Query successful:', data);
    } catch (error) {
      console.error('Query error:', error);
      setChatHistory(prev => [...prev, {
        type: 'ai',
        text: 'Sorry, there was an error processing your question. Make sure backend is running.'
      }]);
    } finally {
      setLoading(false);
      setQuery('');
    }
  };

  return (
    <div style={styles.container}>
      <style>{globalStyles}</style>
      
      <Header 
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        documentsCount={documents.length}
      />

      <div style={styles.content}>
        {activeTab === 'upload' && (
          <div style={styles.grid}>
            <div style={styles.sidebar}>
              <UploadCard
                file={file}
                processing={processing}
                processed={processed}
                onFileUpload={handleFileUpload}
              />
              
              <SentimentCard sentiment={sentiment} />
              
              <MetricsCard summary={summary} />
            </div>

            <ChatInterface
              processed={processed}
              chatHistory={chatHistory}
              loading={loading}
              query={query}
              setQuery={setQuery}
              onQuery={handleQuery}
            />
          </div>
        )}

        {activeTab === 'documents' && (
          <DocumentLibrary 
            documents={documents}
            setActiveTab={setActiveTab}
          />
        )}
      </div>
    </div>
  );
}