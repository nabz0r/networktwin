import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const PerformanceChart = ({ nodes, links }) => {
  const performanceData = nodes.map(node => ({
    name: node.name,
    bandwidth: Math.random() * 100,  // Simulation
    latency: Math.random() * 50      // Simulation
  }));

  return (
    <div className="performance-chart">
      <h2>Performance du Réseau</h2>
      <LineChart width={600} height={300} data={performanceData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="bandwidth" stroke="#8884d8" />
        <Line type="monotone" dataKey="latency" stroke="#82ca9d" />
      </LineChart>
    </div>
  );
};

export default PerformanceChart;