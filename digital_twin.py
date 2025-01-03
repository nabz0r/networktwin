import typing
import numpy as np
import torch
import torch.nn as nn
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class NetworkSliceConfig:
    """Configuration pour un slice réseau"""
    id: str
    type: str = 'default'
    bandwidth: float = 0.0
    latency_target: float = 20.0  # ms
    reliability_target: float = 0.99

class DigitalTwin:
    def __init__(
        self, 
        slice_config: NetworkSliceConfig,
        prediction_model: Optional[nn.Module] = None
    ):
        self.slice_config = slice_config
        self.prediction_model = prediction_model or self._create_default_model()
        
        # États internes du jumeau numérique
        self.historical_data: List[Dict[str, Any]] = []
        self.current_state: Dict[str, Any] = {}
        
    def _create_default_model(self) -> nn.Module:
        """Crée un modèle neuronal bayésien par défaut"""
        class DefaultBayesianModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.layers = nn.Sequential(
                    nn.Linear(10, 64),
                    nn.ReLU(),
                    nn.Linear(64, 32),
                    nn.ReLU(),
                    nn.Linear(32, 1)
                )
            
            def forward(self, x):
                return self.layers(x)
        
        return DefaultBayesianModel()
    
    def update_state(self, new_data: Dict[str, Any]):
        """Met à jour l'état du jumeau numérique"""
        self.historical_data.append(new_data)
        self.current_state = new_data
        
    def predict_resource_allocation(self, input_data: torch.Tensor) -> torch.Tensor:
        """Prédit l'allocation de ressources"""
        with torch.no_grad():
            prediction = self.prediction_model(input_data)
        return prediction
    
    def evaluate_performance(self) -> Dict[str, float]:
        """Évalue les performances du slice réseau"""
        # Logique d'évaluation basée sur les données historiques
        return {
            "bandwidth_utilization": np.mean([d.get('bandwidth', 0) for d in self.historical_data]),
            "latency": np.mean([d.get('latency', 0) for d in self.historical_data]),
            "reliability": np.mean([d.get('reliability', 0) for d in self.historical_data])
        }
    
    def emit_optimization_recommendation(self) -> Dict[str, Any]:
        """Émet des recommandations d'optimisation"""
        performance = self.evaluate_performance()
        
        recommendations = {}
        if performance['bandwidth_utilization'] < 0.6:
            recommendations['bandwidth'] = 'Réduire allocation'
        elif performance['bandwidth_utilization'] > 0.9:
            recommendations['bandwidth'] = 'Augmenter allocation'
        
        if performance['latency'] > self.slice_config.latency_target:
            recommendations['latency'] = 'Optimiser routage'
        
        return recommendations

# Exemple d'utilisation
def main():
    leo_slice_config = NetworkSliceConfig(
        id='leo_satellite_1', 
        type='satellite', 
        bandwidth=100.0,
        latency_target=15.0
    )
    
    leo_twin = DigitalTwin(leo_slice_config)
    
    # Simulation de mise à jour d'état
    leo_twin.update_state({
        'bandwidth': 75.0,
        'latency': 12.5,
        'reliability': 0.995
    })
    
    # Obtenir des recommandations
    recommendations = leo_twin.emit_optimization_recommendation()
    print(recommendations)

if __name__ == "__main__":
    main()