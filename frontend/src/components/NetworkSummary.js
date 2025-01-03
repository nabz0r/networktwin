import React from 'react';

const NetworkSummary = ({ stats }) => {
  return (
    <div className="network-summary">
      <h2>Résumé du Réseau</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Nombre Total de Nœuds</h3>
          <p>{stats.totalNodes}</p>
        </div>
        <div className="stat-card">
          <h3>Nœuds Actifs</h3>
          <p>{stats.activeNodes}</p>
        </div>
        <div className="stat-card">
          <h3>Bande Passante Totale</h3>
          <p>{stats.totalBandwidth.toFixed(2)} Mbps</p>
        </div>
        <div className="stat-card">
          <h3>Latence Moyenne</h3>
          <p>{stats.averageLatency.toFixed(2)} ms</p>
        </div>
      </div>
    </div>
  );
};

export default NetworkSummary;