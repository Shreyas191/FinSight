// API utility functions for backend communication

const API_BASE = 'http://localhost:8000';

// Upload PDF file
export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE}/upload`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Upload failed');
  }

  return await response.json();
};

// Query document
export const queryDocument = async (question, documentIds = null, topK = 5) => {
  const response = await fetch(`${API_BASE}/query`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      question,
      top_k: topK,
      document_ids: documentIds
    }),
  });

  if (!response.ok) {
    throw new Error('Query failed');
  }

  return await response.json();
};

// Get all documents
export const getDocuments = async () => {
  const response = await fetch(`${API_BASE}/documents`);

  if (!response.ok) {
    throw new Error('Failed to fetch documents');
  }

  return await response.json();
};

// Compare documents
export const compareDocuments = async (documentIds, metrics) => {
  const response = await fetch(`${API_BASE}/compare`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      document_ids: documentIds,
      metrics: metrics || ['revenue', 'profit', 'sentiment']
    }),
  });

  if (!response.ok) {
    throw new Error('Comparison failed');
  }

  return await response.json();
};

// Export report as PDF
export const exportReport = async (documentId, options = {}) => {
  const response = await fetch(`${API_BASE}/export`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      document_id: documentId,
      include_summary: options.includeSummary !== false,
      include_qa: options.includeQA !== false,
      include_sentiment: options.includeSentiment !== false,
      include_metrics: options.includeMetrics !== false
    }),
  });

  if (!response.ok) {
    throw new Error('Export failed');
  }

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `financial_analysis_${documentId}.pdf`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(url);
};

// Delete document
export const deleteDocument = async (documentId) => {
  const response = await fetch(`${API_BASE}/document/${documentId}`, {
    method: 'DELETE',
  });

  if (!response.ok) {
    throw new Error('Delete failed');
  }

  return await response.json();
};

// Get advanced metrics
export const getMetrics = async (documentId) => {
  const response = await fetch(`${API_BASE}/metrics/${documentId}`);

  if (!response.ok) {
    throw new Error('Failed to fetch metrics');
  }

  return await response.json();
};

// Health check
export const healthCheck = async () => {
  try {
    const response = await fetch(`${API_BASE}/health`);
    return await response.json();
  } catch (error) {
    return { status: 'offline', error: error.message };
  }
};