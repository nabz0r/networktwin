class NetworkSimulationService {
  generateNetworkTopology(nodeCount = 10) {
    const nodes = [
      { id: 'ground_station', name: 'Station Sol', type: 'ground' },
      ...Array(nodeCount).fill().map((_, i) => ({
        id: `satellite_${i}`, 
        name: `Satellite ${i}`,
        type: 'LEO'
      }))
    ];

    const links = nodes.slice(1).map(node => ({
      source: 'ground_station',
      target: node.id
    }));

    return { nodes, links };
  }

  simulateResourceAllocation(nodes) {
    return nodes.map(node => ({
      ...node,
      bandwidth: Math.random() * 100,
      latency: Math.random() * 20
    }));
  }
}

export default new NetworkSimulationService();