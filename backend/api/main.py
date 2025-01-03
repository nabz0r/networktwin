from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from ..core.network_simulator import NetworkSimulatorOrchestrator

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Orchestrateur de simulation
simulator = NetworkSimulatorOrchestrator()

@app.websocket("/ws/network_simulation")
async def websocket_network_simulation(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Réception des configurations de simulation
            data = await websocket.receive_json()
            network_type = data.get('type', 'leo')

            simulation_result = await simulator.simulate_network(
                network_type=network_type, 
                config=data.get('config', {})
            )

            await websocket.send_json(simulation_result)
    except Exception as e:
        print(f"Erreur de simulation : {e}")
        await websocket.close()

@app.get("/network/topologies")
def get_available_topologies():
    return {
        "types": ["leo", "gns3"],
        "templates": {
            "enterprise": "Topologie entreprise simple",
            "datacenter": "Topologie datacenter",
            "campus": "Réseau campus"
        }
    }