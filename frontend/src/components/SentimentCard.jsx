import React from 'react';
import { styles } from '../styles/styles';

export default function SentimentCard({ sentiment }) {
  if (!sentiment) return null;

  const getSentimentColor = (type) => {
    if (type === 'positive') return '#10b981';
    if (type === 'neutral') return '#fbbf24';
    return '#ef4444';
  };

  return (
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>💭 Sentiment Analysis</h2>
      
      <div style={styles.sentimentContainer}>
        <p style={styles.sentimentLabel}>Overall Sentiment</p>
        <p style={styles.sentimentValue}>{sentiment.overall}</p>
        <p style={styles.sentimentScore}>
          Confidence: {Math.round(sentiment.score * 100)}%
        </p>
      </div>

      <div>
        {Object.entries(sentiment.breakdown).map(([key, value]) => (
          <div key={key} style={{ marginBottom: '0.75rem' }}>
            <div style={styles.sentimentBarLabel}>
              <span style={{ textTransform: 'capitalize' }}>{key}</span>
              <span>{value}%</span>
            </div>
            <div style={styles.sentimentBar}>
              <div style={{
                height: '100%',
                width: `${value}%`,
                background: getSentimentColor(key),
                transition: 'width 0.3s'
              }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}