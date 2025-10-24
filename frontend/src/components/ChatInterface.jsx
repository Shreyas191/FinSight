import React from 'react';
import { styles } from '../styles/styles';

export default function ChatInterface({ 
  processed, 
  chatHistory, 
  loading, 
  query, 
  setQuery, 
  onQuery 
}) {
  const suggestedQuestions = [
    'What was the total revenue and how did it grow?',
    'What are the main business risks identified?',
    'How did profit margins change?'
  ];

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onQuery();
    }
  };

  return (
    <div style={styles.card}>
      <div style={styles.chatContainer}>
        <div style={styles.chatHeader}>
          <h2 style={{ ...styles.cardTitle, marginBottom: 0 }}>
            💬 Ask Questions
          </h2>
          <p style={{ fontSize: '0.875rem', color: '#c4b5fd', margin: '0.25rem 0 0 0' }}>
            Query financial data, analyze risks, compare metrics
          </p>
        </div>

        <div style={styles.chatMessages}>
          {!processed ? (
            <div style={styles.emptyState}>
              <div style={{
                display: 'inline-block',
                padding: '1rem',
                background: 'rgba(255,255,255,0.05)',
                borderRadius: '1rem',
                marginBottom: '1rem'
              }}>
                <div style={{ fontSize: '3rem' }}>📄</div>
              </div>
              <p style={styles.emptyTitle}>Upload a report to get started</p>
              <p style={{ fontSize: '0.875rem', color: '#c4b5fd', margin: 0 }}>
                AI will analyze and answer your questions instantly
              </p>
            </div>
          ) : chatHistory.length === 0 ? (
            <div>
              <p style={{ marginBottom: '1rem', color: '#c4b5fd' }}>
                💡 Suggested questions:
              </p>
              {suggestedQuestions.map((suggestion, i) => (
                <button
                  key={i}
                  onClick={() => setQuery(suggestion)}
                  style={styles.suggestionBtn}
                  onMouseOver={(e) => {
                    e.target.style.background = 'rgba(255,255,255,0.1)';
                    e.target.style.borderColor = '#a855f7';
                  }}
                  onMouseOut={(e) => {
                    e.target.style.background = 'rgba(255,255,255,0.05)';
                    e.target.style.borderColor = 'rgba(255,255,255,0.1)';
                  }}
                >
                  {suggestion}
                </button>
              ))}
            </div>
          ) : (
            <>
              {chatHistory.map((msg, i) => (
                <div 
                  key={i} 
                  style={msg.type === 'user' ? styles.messageUser : styles.messageAi}
                >
                  {msg.text}
                </div>
              ))}
              {loading && (
                <div style={styles.messageAi}>
                  <div style={styles.loading} />
                </div>
              )}
            </>
          )}
        </div>

        <div style={styles.chatInputContainer}>
          <input
            type="text"
            style={styles.chatInput}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder={
              processed 
                ? "Ask about revenue, risks, profits..." 
                : "Upload a document first..."
            }
            disabled={!processed || loading}
          />
          <button
            style={{
              ...styles.btnPrimary,
              opacity: (!processed || !query.trim() || loading) ? 0.5 : 1,
              cursor: (!processed || !query.trim() || loading) ? 'not-allowed' : 'pointer'
            }}
            onClick={onQuery}
            disabled={!processed || !query.trim() || loading}
          >
            {loading ? <div style={styles.loading} /> : '🔍'}
          </button>
        </div>
      </div>
    </div>
  );
}