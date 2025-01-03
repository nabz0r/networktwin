import React, { useState, useEffect } from 'react';
import NetworkSummary from './NetworkSummary';
import PerformanceChart from './PerformanceChart';
import NetworkSimulationService from '../services/networkSimulationService';

const Dashboard = () => {
  const [networkStats, setNetworkStats] = useState({
    totalNodes: 0,
    activeNodes: 0,
    totalBandwidth: 0,
    averageLatency: 0
  });

  const [networkTopology, setNetworkTopology] = useState({
    nodes: [],
    links: []
  });

  useEffect(() => {
    const topology = NetworkSimulationService.generateNetworkTopology();
    setNetworkTopology(topology);

    const stats = {
      totalNodes: topology.nodes.length,
      activeNodes: topology.nodes.filter(node => node.type === 'LEO').length,
      totalBandwidth: topology.nodes.reduce((sum, node) => 
        sum + (node.bandwidth || 0), 0),
      averageLatency: topology.nodes.reduce((sum, node) => 
        sum + (node.latency || 0), 0) / topology.nodes.length
    };

    setNetworkStats(stats);
  }, []);

  return (
    <div className="dashboard">
      <h1>NetworkTwin - Tableau de Bord</h1>
      <NetworkSummary stats={networkStats} />
      <PerformanceChart 
        nodes={networkTopology.nodes} 
        links={networkTopology.links}
      />
    </div>
  );
};

export default Dashboard;