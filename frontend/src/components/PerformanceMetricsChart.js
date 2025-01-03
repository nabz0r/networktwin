import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';

const PerformanceMetricsChart = ({ metrics }) => {
    const chartData = [
        { name: 'Bande Passante', value: metrics.bandwidth },
        { name: 'Latence', value: metrics.latency },
        { name: 'Fiabilité', value: metrics.reliability * 100 }
    ];

    return (
        <div>
            <h3>Métriques de Performance du Réseau</h3>
            <BarChart width={600} height={300} data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="value" fill="#8884d8" />
            </BarChart>
        </div>
    );
};

export default PerformanceMetricsChart;