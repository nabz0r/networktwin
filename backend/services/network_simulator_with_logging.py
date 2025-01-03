import logging
from ..config.logging_config import log_performance

class NetworkSimulatorWithLogging:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    @log_performance
    def generate_topology(self, num_satellites=10):
        self.logger.info(f"Generating network topology with {num_satellites} satellites")
        # Simulation de génération de topologie
        satellites = [
            {
                'id': f'satellite_{i}',
                'bandwidth': random.uniform(50, 200),
                'latency': random.uniform(5, 25)
            } for i in range(num_satellites)
        ]
        return satellites
    
    def log_network_event(self, event_type, details):
        """Méthode générique pour logger des événements réseau"""
        self.logger.info(f"Network Event: {event_type} - {details}")