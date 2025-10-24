// All inline styles for the application

export const styles = {
  // Main container
  container: {
    minHeight: '100vh',
    background: 'linear-gradient(135deg, #0f172a 0%, #581c87 50%, #0f172a 100%)',
    color: 'white',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
  },

  // Header
  header: {
    background: 'rgba(0, 0, 0, 0.2)',
    backdropFilter: 'blur(10px)',
    borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
    padding: '1.5rem 2rem'
  },
  headerContent: {
    maxWidth: '1400px',
    margin: '0 auto',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: '1rem'
  },
  logoSection: {
    display: 'flex',
    alignItems: 'center',
    gap: '1rem'
  },
  logoIcon: {
    width: '48px',
    height: '48px',
    background: 'linear-gradient(135deg, #a855f7, #ec4899)',
    borderRadius: '12px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '24px'
  },
  title: {
    fontSize: '1.5rem',
    fontWeight: '700',
    margin: 0
  },
  subtitle: {
    fontSize: '0.875rem',
    color: '#c4b5fd',
    margin: '0.25rem 0 0 0'
  },

  // Navigation
  navButtons: {
    display: 'flex',
    gap: '1rem'
  },
  navBtn: {
    padding: '0.75rem 1.5rem',
    borderRadius: '0.5rem',
    fontWeight: '500',
    border: 'none',
    cursor: 'pointer',
    transition: 'all 0.2s',
    fontSize: '0.875rem'
  },
  navBtnActive: {
    background: '#a855f7',
    color: 'white'
  },
  navBtnInactive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#c4b5fd'
  },

  // Layout
  content: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '2rem'
  },
  grid: {
    display: 'grid',
    gap: '1.5rem',
    gridTemplateColumns: '1fr 2fr'
  },
  sidebar: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1.5rem'
  },

  // Cards
  card: {
    background: 'rgba(255, 255, 255, 0.1)',
    backdropFilter: 'blur(20px)',
    borderRadius: '1rem',
    padding: '1.5rem',
    border: '1px solid rgba(255, 255, 255, 0.2)',
    boxShadow: '0 20px 50px rgba(0, 0, 0, 0.3)'
  },
  cardTitle: {
    fontSize: '1.125rem',
    fontWeight: '600',
    marginBottom: '1rem',
    display: 'flex',
    alignItems: 'center',
    gap: '0.5rem'
  },

  // Upload zone
  uploadZone: {
    border: '2px dashed rgba(168, 85, 247, 0.5)',
    borderRadius: '0.75rem',
    padding: '3rem',
    textAlign: 'center',
    cursor: 'pointer',
    transition: 'all 0.2s'
  },
  uploadIcon: {
    fontSize: '3rem',
    marginBottom: '1rem'
  },
  uploadText: {
    fontWeight: 500,
    marginBottom: '0.5rem'
  },
  uploadSubtext: {
    fontSize: '0.875rem',
    color: '#c4b5fd'
  },

  // Metrics
  metricsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '0.75rem'
  },
  metricCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    padding: '1rem',
    borderRadius: '0.5rem'
  },
  metricLabel: {
    fontSize: '0.75rem',
    color: '#c4b5fd',
    textTransform: 'uppercase',
    letterSpacing: '0.05em',
    marginBottom: '0.5rem'
  },
  metricValue: {
    fontSize: '0.875rem',
    fontWeight: '600'
  },

  // Sentiment
  sentimentContainer: {
    textAlign: 'center',
    padding: '1rem',
    background: 'rgba(255,255,255,0.05)',
    borderRadius: '0.75rem',
    marginBottom: '1rem'
  },
  sentimentLabel: {
    fontSize: '0.875rem',
    color: '#c4b5fd',
    marginBottom: '0.5rem'
  },
  sentimentValue: {
    fontSize: '2rem',
    fontWeight: 700,
    textTransform: 'capitalize',
    margin: 0
  },
  sentimentScore: {
    fontSize: '0.875rem',
    color: '#c4b5fd',
    marginTop: '0.5rem'
  },
  sentimentBar: {
    height: '0.5rem',
    background: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '0.25rem',
    overflow: 'hidden',
    marginTop: '0.5rem'
  },
  sentimentBarLabel: {
    display: 'flex',
    justifyContent: 'space-between',
    fontSize: '0.875rem',
    marginBottom: '0.5rem'
  },

  // Chat
  chatContainer: {
    display: 'flex',
    flexDirection: 'column',
    height: 'calc(100vh - 250px)'
  },
  chatHeader: {
    padding: '1.5rem',
    borderBottom: '1px solid rgba(255,255,255,0.2)'
  },
  chatMessages: {
    flex: 1,
    overflowY: 'auto',
    padding: '1.5rem',
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem'
  },
  messageUser: {
    alignSelf: 'flex-end',
    maxWidth: '85%',
    padding: '1rem',
    borderRadius: '1rem',
    background: 'linear-gradient(135deg, #a855f7, #ec4899)',
    fontSize: '0.875rem',
    lineHeight: '1.5'
  },
  messageAi: {
    alignSelf: 'flex-start',
    maxWidth: '85%',
    padding: '1rem',
    borderRadius: '1rem',
    background: 'rgba(255, 255, 255, 0.1)',
    border: '1px solid rgba(255, 255, 255, 0.2)',
    fontSize: '0.875rem',
    lineHeight: '1.5'
  },
  chatInputContainer: {
    padding: '1.5rem',
    borderTop: '1px solid rgba(255, 255, 255, 0.2)',
    display: 'flex',
    gap: '0.75rem'
  },
  chatInput: {
    flex: 1,
    padding: '0.75rem 1rem',
    background: 'rgba(255, 255, 255, 0.1)',
    border: '1px solid rgba(255, 255, 255, 0.2)',
    borderRadius: '0.75rem',
    color: 'white',
    fontSize: '0.875rem',
    outline: 'none'
  },

  // Buttons
  btnPrimary: {
    padding: '0.75rem 1.5rem',
    background: 'linear-gradient(135deg, #a855f7, #ec4899)',
    color: 'white',
    border: 'none',
    borderRadius: '0.75rem',
    fontWeight: '500',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '0.5rem',
    transition: 'all 0.2s'
  },
  suggestionBtn: {
    width: '100%',
    textAlign: 'left',
    padding: '1rem',
    background: 'rgba(255, 255, 255, 0.05)',
    border: '1px solid rgba(255, 255, 255, 0.1)',
    borderRadius: '0.75rem',
    color: 'white',
    cursor: 'pointer',
    transition: 'all 0.2s',
    fontSize: '0.875rem',
    marginBottom: '0.5rem'
  },

  // Loading
  loading: {
    display: 'inline-block',
    width: '1.25rem',
    height: '1.25rem',
    border: '2px solid rgba(255, 255, 255, 0.3)',
    borderTopColor: 'white',
    borderRadius: '50%',
    animation: 'spin 0.6s linear infinite'
  },

  // Documents
  documentGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
    gap: '1.5rem',
    marginTop: '1.5rem'
  },
  docCard: {
    background: 'rgba(255, 255, 255, 0.1)',
    border: '2px solid rgba(255, 255, 255, 0.2)',
    borderRadius: '1rem',
    padding: '1.5rem',
    cursor: 'pointer',
    transition: 'all 0.2s'
  },

  // Empty state
  emptyState: {
    textAlign: 'center',
    padding: '5rem 2rem'
  },
  emptyIcon: {
    fontSize: '4rem',
    opacity: 0.3,
    marginBottom: '1rem'
  },
  emptyTitle: {
    fontSize: '1.125rem',
    marginBottom: '0.5rem'
  },
  emptySubtitle: {
    fontSize: '0.875rem',
    color: '#c4b5fd',
    marginBottom: '1.5rem'
  }
};

// CSS for animations
export const globalStyles = `
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
  
  input[type="file"] {
    display: none;
  }
  
  * {
    box-sizing: border-box;
  }
`;