import React, { useState, useEffect } from 'react';
import LEOConstellationVisualization from '../components/LEOConstellationVisualization';
import PerformanceMetricsChart from '../components/PerformanceMetricsChart';
import SatelliteHealthMonitor from '../components/SatelliteHealthMonitor';

const LEONetworkDashboard = () => {
    const [networkData, setNetworkData] = useState(null);

    useEffect(() => {
        // Simulation de récupération de données
        const fetchNetworkData = async () => {
            // TODO: Remplacer par un vrai appel à l'API backend
            const response = await fetch('/api/leo-network-simulation');
            const data = await response.json();
            setNetworkData(data);
        };

        const intervalId = setInterval(fetchNetworkData, 5000);
        return () => clearInterval(intervalId);
    }, []);

    if (!networkData) return <div>Chargement...</div>;

    return (
        <div className="leo-network-dashboard">
            <h1>Tableau de Bord Constellation LEO</h1>
            
            <div className="visualization-grid">
                <LEOConstellationVisualization 
                    satellites={networkData.constellation}
                />
                
                <PerformanceMetricsChart 
                    metrics={networkData.predicted_performance}
                />
                
                <SatelliteHealthMonitor 
                    satellites={networkData.constellation}
                />
            </div>
        </div>
    );
};

export default LEONetworkDashboard;