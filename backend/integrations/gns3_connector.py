import requests
import json
from typing import Dict, List, Optional

class GNS3Connector:
    def __init__(self, host='localhost', port=3080):
        self.base_url = f'http://{host}:{port}'
        self.session_id = None
    
    def connect(self, project_name: str = 'NetworkTwin'):
        """Connexion et création/récupération d'un projet"""
        try:
            # Récupérer les projets existants
            projects_response = requests.get(f'{self.base_url}/v2/projects')
            projects = projects_response.json()

            # Chercher un projet existant
            existing_project = next((p for p in projects if p['name'] == project_name), None)

            if existing_project:
                self.session_id = existing_project['project_id']
            else:
                # Créer un nouveau projet
                new_project_data = {
                    'name': project_name,
                    'path': f'/opt/gns3/projects/{project_name}'
                }
                new_project_response = requests.post(f'{self.base_url}/v2/projects', json=new_project_data)
                self.session_id = new_project_response.json()['project_id']

            return self.session_id
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            return None

    def add_node(self, node_type: str, name: str, template_id: Optional[str] = None) -> Dict:
        """Ajout d'un nœud réseau"""
        if not self.session_id:
            raise ValueError("Pas de session active")

        node_data = {
            'name': name,
            'node_type': node_type,
            'project_id': self.session_id
        }

        if template_id:
            node_data['template_id'] = template_id

        response = requests.post(f'{self.base_url}/v2/projects/{self.session_id}/nodes', json=node_data)
        return response.json()

    def add_link(self, source_node_id: str, source_adapter: str, 
                 destination_node_id: str, destination_adapter: str) -> Dict:
        """Création d'un lien entre deux nœuds"""
        link_data = {
            'nodes': [
                {
                    'node_id': source_node_id,
                    'adapter': source_adapter
                },
                {
                    'node_id': destination_node_id,
                    'adapter': destination_adapter
                }
            ]
        }

        response = requests.post(f'{self.base_url}/v2/projects/{self.session_id}/links', json=link_data)
        return response.json()

    def start_project(self):
        """Démarrage du projet de simulation"""
        if not self.session_id:
            raise ValueError("Pas de session active")
        
        response = requests.post(f'{self.base_url}/v2/projects/{self.session_id}/open')
        return response.status_code == 200

    def stop_project(self):
        """Arrêt du projet de simulation"""
        if not self.session_id:
            raise ValueError("Pas de session active")
        
        response = requests.post(f'{self.base_url}/v2/projects/{self.session_id}/close')
        return response.status_code == 200

    def get_topology_summary(self) -> Dict:
        """Récupération d'un résumé de la topologie"""
        if not self.session_id:
            raise ValueError("Pas de session active")
        
        response = requests.get(f'{self.base_url}/v2/projects/{self.session_id}/nodes')
        nodes = response.json()

        response = requests.get(f'{self.base_url}/v2/projects/{self.session_id}/links')
        links = response.json()

        return {
            'nodes': nodes,
            'links': links
        }