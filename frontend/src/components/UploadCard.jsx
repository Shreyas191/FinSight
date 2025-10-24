import React from 'react';
import { styles } from '../styles/styles';

export default function UploadCard({ file, processing, processed, onFileUpload }) {
  return (
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>📤 Upload Report</h2>
      <label>
        <input 
          type="file" 
          accept="application/pdf" 
          onChange={onFileUpload}
        />
        <div style={styles.uploadZone}>
          {!file ? (
            <>
              <div style={styles.uploadIcon}>📄</div>
              <p style={styles.uploadText}>Click to upload PDF</p>
              <p style={styles.uploadSubtext}>Annual reports, 10-K, earnings</p>
            </>
          ) : (
            <>
              <div style={styles.uploadIcon}>
                {processing ? '⏳' : '✅'}
              </div>
              <p style={styles.uploadText}>{file.name}</p>
              <p style={{ ...styles.uploadSubtext, marginTop: '0.5rem' }}>
                {processing ? 'Processing document...' : processed ? 'Ready to analyze!' : 'Uploading...'}
              </p>
            </>
          )}
        </div>
      </label>
    </div>
  );
}