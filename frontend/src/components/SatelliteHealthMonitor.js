import React from 'react';
import { RadialBarChart, RadialBar, Legend } from 'recharts';

const SatelliteHealthMonitor = ({ satellites }) => {
    const healthData = satellites.map(sat => ({
        name: sat.id,
        health: sat.health * 100,
        fill: getSatelliteHealthColor(sat.health)
    }));

    const getSatelliteHealthColor = (health) => {
        if (health > 0.9) return '#00C49F'; // Vert (très bon)
        if (health > 0.7) return '#FFBB28'; // Jaune (moyen)
        return '#FF8042'; // Rouge (critique)
    };

    return (
        <div>
            <h3>Santé des Satellites</h3>
            <RadialBarChart
                width={500}
                height={300}
                innerRadius="10%"
                outerRadius="90%"
                data={healthData}
                startAngle={180}
                endAngle={0}
            >
                <RadialBar dataKey="health" label={{ fill: '#666', position: 'insideStart' }} />
                <Legend iconSize={10} width={120} height={140} layout="vertical" />
            </RadialBarChart>
        </div>
    );
};

export default SatelliteHealthMonitor;