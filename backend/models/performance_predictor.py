import torch
import torch.nn as nn
import numpy as np

class PerformancePredictor(nn.Module):
    def __init__(self, input_size=10, hidden_size=64, output_size=3):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        """Prédit les performances du réseau
        
        Args:
            x (torch.Tensor): Caractéristiques d'entrée
        
        Returns:
            torch.Tensor: Prédictions de performances
            - Bande passante
            - Latence
            - Fiabilité
        """
        return self.network(x)
    
    def predict_network_performance(self, constellation):
        """Convertit une constellation en tenseur prédictible"""
        features = []
        for sat in constellation.satellites:
            sat_features = [
                sat.bandwidth,
                sat.latency,
                sat.reliability,
                sat.health
            ]
            features.append(sat_features)
        
        # Padding ou troncature pour taille fixe
        features = features[:10]  # Limite à 10 satellites
        while len(features) < 10:
            features.append([0, 0, 0, 0])
        
        input_tensor = torch.FloatTensor(features).flatten()
        predictions = self(input_tensor)
        
        return {
            'bandwidth': predictions[0].item(),
            'latency': predictions[1].item(),
            'reliability': predictions[2].item()
        }