import asyncio
from typing import Dict, Any, List
from ..integrations.gns3_connector import GNS3Connector
from ..integrations.leo_network import LEONetworkSimulator

class NetworkSimulatorOrchestrator:
    def __init__(self):
        self.gns3_connector = GNS3Connector()
        self.leo_simulator = LEONetworkSimulator()
        self.active_simulations = {}

    async def simulate_network(self, network_type: str, config: Dict) -> Dict[str, Any]:
        """
        Simulation centralisée pour différents types de réseaux
        """
        if network_type == 'leo':
            return await self._simulate_leo_network(config)
        elif network_type == 'gns3':
            return await self._simulate_gns3_network(config)
        else:
            raise ValueError(f"Type de réseau non supporté : {network_type}")

    async def _simulate_leo_network(self, config: Dict) -> Dict[str, Any]:
        constellation = self.leo_simulator.simulate_network_dynamics()
        return {
            'type': 'leo',
            'topology': constellation,
            'performance_metrics': self.leo_simulator.performance_predictor.predict_network_performance()
        }

    async def _simulate_gns3_network(self, config: Dict) -> Dict[str, Any]:
        project_id = self.gns3_connector.connect(config.get('project_name', 'NetworkTwin'))
        
        # Ajout dynamique de nœuds selon la configuration
        for node in config.get('nodes', []):
            self.gns3_connector.add_node(
                node_type=node.get('type'),
                name=node.get('name')
            )

        return {
            'type': 'gns3',
            'project_id': project_id,
            'topology': self.gns3_connector.get_topology_summary()
        }

    async def run_continuous_simulation(self, interval: int = 10):
        """
        Simulation continue avec mises à jour périodiques
        """
        while True:
            leo_sim = await self._simulate_leo_network({})
            # Logique de stockage/notification
            await asyncio.sleep(interval)