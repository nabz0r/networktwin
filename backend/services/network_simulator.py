import random
import numpy as np
import networkx as nx
from ..models.network import NetworkTopology, Node

class NetworkSimulator:
    def __init__(self, num_satellites=10, num_ground_stations=2):
        self.graph = nx.random_geometric_graph(num_satellites, 0.5)
        self.ground_stations = []
        self.satellites = []
        self._generate_network()

    def _generate_network(self):
        # Génération de stations au sol
        for i in range(2):
            ground_station = Node(
                id=f'ground_station_{i}',
                name=f'Ground Station {i}',
                type='ground',
                bandwidth=random.uniform(100, 500),
                latency=random.uniform(10, 50)
            )
            self.ground_stations.append(ground_station)

        # Génération de satellites
        for node_id in self.graph.nodes:
            satellite = Node(
                id=f'satellite_{node_id}',
                name=f'Satellite {node_id}',
                type='LEO',
                bandwidth=random.uniform(50, 200),
                latency=random.uniform(5, 25),
                reliability=random.uniform(0.9, 1.0)
            )
            self.satellites.append(satellite)

    def get_topology(self):
        links = [{'source': node.id, 'target': ground.id} 
                 for node in self.satellites 
                 for ground in self.ground_stations]
        
        return NetworkTopology(
            nodes=self.ground_stations + self.satellites,
            links=links
        )

    def update_topology(self):
        # Simulation de changements dynamiques
        for satellite in self.satellites:
            satellite.bandwidth = random.uniform(50, 200)
            satellite.latency = random.uniform(5, 25)
            satellite.reliability = random.uniform(0.9, 1.0)
        
        return self.get_topology()