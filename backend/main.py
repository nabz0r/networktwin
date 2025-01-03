import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from services.websocket_manager import WebSocketManager
from services.network_simulator import NetworkSimulator

app = FastAPI()

# Configuration CORS pour autoriser les connexions du frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

network_simulator = NetworkSimulator()
websocket_manager = WebSocketManager()

@app.websocket("/ws/network")
async def websocket_network_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    try:
        while True:
            # Attendre un message du client si nécessaire
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(websocket_manager.broadcast_network_updates(network_simulator))

@app.get("/network/topology")
def get_initial_topology():
    return network_simulator.get_topology().model_dump()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)