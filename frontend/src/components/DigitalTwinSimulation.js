import React, { useState, useEffect } from 'react';
import { ForceGraph2D } from 'react-force-graph';
import MQTTService from '../services/mqttService';
import NetworkSimulationService from '../services/networkSimulationService';

const DigitalTwinSimulation = () => {
  const [networkData, setNetworkData] = useState({
    nodes: [],
    links: []
  });

  useEffect(() => {
    const topologyData = NetworkSimulationService.generateNetworkTopology();
    setNetworkData(topologyData);

    MQTTService.connect()
      .then(() => {
        MQTTService.subscribe('network/topology');
        MQTTService.onMessage((topic, message) => {
          if (topic === 'network/topology') {
            console.log('Topology Update', message);
          }
        });
      });

    return () => {
      // Cleanup
    };
  }, []);

  return (
    <div>
      <h2>Simulation Topologie Réseau</h2>
      <ForceGraph2D
        graphData={networkData}
        nodeLabel="name"
        nodeColor={node => 
          node.type === 'LEO' ? 'blue' : 'green'
        }
      />
    </div>
  );
};

export default DigitalTwinSimulation;