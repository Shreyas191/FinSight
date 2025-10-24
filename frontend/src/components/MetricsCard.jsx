import React from 'react';
import { styles } from '../styles/styles';

export default function MetricsCard({ summary }) {
  if (!summary) return null;

  const metrics = [
    { label: 'Revenue', value: summary.revenue },
    { label: 'Net Profit', value: summary.profit },
    { label: 'Margin', value: summary.profitMargin },
    { label: 'EPS', value: summary.eps }
  ];

  return (
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>📈 Financial Highlights</h2>
      
      <div style={styles.metricsGrid}>
        {metrics.map((metric, index) => (
          <div key={index} style={styles.metricCard}>
            <div style={styles.metricLabel}>{metric.label}</div>
            <div style={styles.metricValue}>{metric.value}</div>
          </div>
        ))}
      </div>
    </div>
  );
}