import React from 'react';
import NetworkSummary from './NetworkSummary';
import PerformanceChart from './PerformanceChart';
import useNetworkUpdates from '../hooks/useNetworkUpdates';

const Dashboard = () => {
  const networkData = useNetworkUpdates();

  const networkStats = {
    totalNodes: networkData.nodes.length,
    activeNodes: networkData.nodes.filter(node => node.type === 'LEO').length,
    totalBandwidth: networkData.nodes.reduce((sum, node) => 
      sum + (node.bandwidth || 0), 0),
    averageLatency: networkData.nodes.reduce((sum, node) => 
      sum + (node.latency || 0), 0) / (networkData.nodes.length || 1)
  };

  return (
    <div className="dashboard">
      <h1>NetworkTwin - Tableau de Bord Temps Réel</h1>
      <NetworkSummary stats={networkStats} />
      <PerformanceChart 
        nodes={networkData.nodes} 
        links={networkData.links}
      />
    </div>
  );
};

export default Dashboard;