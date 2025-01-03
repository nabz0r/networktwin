# 🛰️ NetworkTwin - Documentation Technique

## Architecture Système

### Vue d'Ensemble
NetworkTwin est une plateforme de simulation et de modélisation réseau avancée, conçue pour offrir une flexibilité maximale dans la simulation de différents types de réseaux.

### Composants Principaux
- **Backend** : Python (FastAPI)
- **Frontend** : React.js
- **Simulation** : Multi-type (LEO, GNS3)
- **Communication** : WebSocket

## Configuration

### Fichier de Configuration Global
```yaml
simulation:
  default_network_type: leo
  update_interval: 10

gns3:
  host: localhost
  port: 3080
  default_project: NetworkTwin
```

## Types de Réseaux Supportés
- Satellites LEO
- Topologies GNS3
- Réseaux d'entreprise
- Datacenters

## Installation

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

## Contact
nabz0r@gmail.com