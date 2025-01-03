# 🛰️ NetworkTwin - Documentation Technique

## Architecture Système

### Vue d'Ensemble
NetworkTwin est une plateforme de simulation et de modélisation réseau avancée, conçue pour offrir une flexibilité maximale dans la simulation de différents types de réseaux.

### Composants Principaux
- **Backend** : Python (FastAPI)
- **Frontend** : React.js
- **Simulation** : Multi-type (LEO, GNS3)
- **Communication** : WebSocket

## Architecture Technique Détaillée

### Backend
#### Modules Principaux
1. `core/network_simulator.py`
   - Orchestrateur principal de simulation
   - Gestion des différents types de réseaux
   - Intégration des simulateurs spécifiques

2. `integrations/`
   - `gns3_connector.py` : Connexion à l'API GNS3
   - `leo_network.py` : Simulation de réseaux satellitaires

3. `api/main.py`
   - Point d'entrée FastAPI
   - Gestion des websockets
   - Routing des simulations

### Frontend
#### Services d'Intégration
1. `network_integration.js`
   - Gestion de la communication WebSocket
   - Méthodes de simulation réseau

#### Composants
- Visualisation de topologies
- Tableau de bord dynamique
- Interfaces de configuration

## Protocoles de Communication

### WebSocket
- Endpoint : `/ws/network_simulation`
- Protocol : JSON
- Bidirectionnel

### Flux de Données
```
Client (Frontend) 
    ↓ WebSocket 
API FastAPI 
    ↓ 
Orchestrateur de Simulation 
    ↓ 
Simulateurs Spécifiques (LEO, GNS3)
```

## Configuration

### Fichier de Configuration Global
`config/network_twin_config.yaml`

```yaml
simulation:
  default_network_type: leo
  update_interval: 10

gns3:
  host: localhost
  port: 3080
  default_project: NetworkTwin

prediction:
  model_type: bayesian
  confidence_level: 0.95

logging:
  level: INFO
  file: /var/log/networktwin/simulation.log
```

## Types de Réseaux Supportés
- Satellites LEO
- Topologies GNS3
- Réseaux d'entreprise
- Datacenters

## Modèles de Simulation

### Modèle LEO
- Génération dynamique de constellations
- Prédiction de performances
- Simulation de santé des satellites

### Modèle GNS3
- Création de topologies réseau
- Simulation d'équipements réels
- Support multi-constructeurs

## API Endpoints

### WebSocket `/ws/network_simulation`
#### Requête
```json
{
  "type": "leo",
  "config": {
    "constellation_size": 20,
    "altitude": 550
  }
}
```

#### Réponse
```json
{
  "type": "leo",
  "topology": {...},
  "performance_metrics": {...}
}
```

## Installation et Démarrage

### Prérequis
- Python 3.10+
- Node.js 18+
- GNS3 (optionnel)

### Backend
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.api.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Contribution

### Processus
1. Fork du repository
2. Créer une branche de feature
3. Soumettre une Pull Request
4. Revue de code

## Licence
MIT License

## Contact
nabz0r@gmail.com
