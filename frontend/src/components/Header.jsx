import React from 'react';
import { styles } from '../styles/styles';

export default function Header({ activeTab, setActiveTab, documentsCount }) {
  return (
    <div style={styles.header}>
      <div style={styles.headerContent}>
        <div style={styles.logoSection}>
          <div style={styles.logoIcon}>📊</div>
          <div>
            <h1 style={styles.title}>Financial Report Analyzer Pro</h1>
            <p style={styles.subtitle}>AI-powered insights from annual reports</p>
          </div>
        </div>
        
        <div style={styles.navButtons}>
          <button
            onClick={() => setActiveTab('upload')}
            style={{
              ...styles.navBtn,
              ...(activeTab === 'upload' ? styles.navBtnActive : styles.navBtnInactive)
            }}
          >
            Upload
          </button>
          <button
            onClick={() => setActiveTab('documents')}
            style={{
              ...styles.navBtn,
              ...(activeTab === 'documents' ? styles.navBtnActive : styles.navBtnInactive)
            }}
          >
            📁 Documents ({documentsCount})
          </button>
        </div>
      </div>
    </div>
  );
}