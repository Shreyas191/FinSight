import React from 'react';
import { styles } from '../styles/styles';

export default function DocumentLibrary({ documents, setActiveTab }) {
  return (
    <div>
      <div style={styles.card}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 700, margin: '0 0 0.5rem 0' }}>
          📚 Document Library
        </h2>
        <p style={{ fontSize: '0.875rem', color: '#c4b5fd', margin: 0 }}>
          Manage your uploaded financial reports
        </p>
      </div>

      {documents.length === 0 ? (
        <div style={{ 
          ...styles.card, 
          ...styles.emptyState, 
          marginTop: '1.5rem' 
        }}>
          <div style={styles.emptyIcon}>📁</div>
          <p style={styles.emptyTitle}>No documents uploaded yet</p>
          <p style={styles.emptySubtitle}>
            Upload your first financial report to get started
          </p>
          <button
            onClick={() => setActiveTab('upload')}
            style={styles.btnPrimary}
          >
            Upload Document
          </button>
        </div>
      ) : (
        <div style={styles.documentGrid}>
          {documents.map((doc) => (
            <div key={doc.id} style={styles.docCard}>
              <div style={{ marginBottom: '1rem' }}>
                <h3 style={{ 
                  fontSize: '0.875rem', 
                  fontWeight: 600, 
                  marginBottom: '0.5rem',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem'
                }}>
                  📄 {doc.filename}
                </h3>
                <p style={{ fontSize: '0.75rem', color: '#c4b5fd' }}>
                  {new Date(doc.uploadDate).toLocaleDateString()}
                </p>
              </div>

              <div style={styles.metricsGrid}>
                <div style={styles.metricCard}>
                  <div style={{ fontSize: '0.75rem', color: '#c4b5fd', marginBottom: '0.5rem' }}>
                    Revenue
                  </div>
                  <div style={{ fontSize: '0.875rem', fontWeight: 600 }}>
                    {doc.summary.revenue}
                  </div>
                </div>
                <div style={styles.metricCard}>
                  <div style={{ fontSize: '0.75rem', color: '#c4b5fd', marginBottom: '0.5rem' }}>
                    Profit
                  </div>
                  <div style={{ fontSize: '0.875rem', fontWeight: 600 }}>
                    {doc.summary.profit}
                  </div>
                </div>
                <div style={styles.metricCard}>
                  <div style={{ fontSize: '0.75rem', color: '#c4b5fd', marginBottom: '0.5rem' }}>
                    Sentiment
                  </div>
                  <div style={{ 
                    fontSize: '0.875rem', 
                    fontWeight: 600,
                    textTransform: 'capitalize'
                  }}>
                    {doc.sentiment.overall}
                  </div>
                </div>
                <div style={styles.metricCard}>
                  <div style={{ fontSize: '0.75rem', color: '#c4b5fd', marginBottom: '0.5rem' }}>
                    Margin
                  </div>
                  <div style={{ fontSize: '0.875rem', fontWeight: 600 }}>
                    {doc.summary.profitMargin}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}