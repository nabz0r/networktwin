from dataclasses import dataclass, field
from typing import List, Optional
import numpy as np
import torch
import torch.nn as nn

@dataclass
class Satellite:
    id: str
    altitude: float = 550  # km
    position: Optional[List[float]] = None
    bandwidth: float = 0.0
    latency: float = 0.0
    reliability: float = 1.0
    health: float = 1.0  # Santé du satellite

@dataclass
class LEOConstellation:
    satellites: List[Satellite] = field(default_factory=list)
    num_planes: int = 6
    satellites_per_plane: int = 22
    inclination: float = 53.0  # degrés

    def generate_constellation(self):
        """Génère une constellation LEO réaliste"""
        satellites = []
        for plane in range(self.num_planes):
            for sat in range(self.satellites_per_plane):
                satellite_id = f'sat_{plane}_{sat}'
                
                # Simulation de positions et caractéristiques
                position = [
                    np.random.uniform(-1, 1),
                    np.random.uniform(-1, 1),
                    np.random.uniform(-1, 1)
                ]
                
                satellite = Satellite(
                    id=satellite_id,
                    position=position,
                    bandwidth=np.random.uniform(50, 200),
                    latency=np.random.uniform(20, 50),
                    reliability=np.random.uniform(0.95, 1.0),
                    health=np.random.uniform(0.9, 1.0)
                )
                satellites.append(satellite)
        
        self.satellites = satellites
        return self.satellites