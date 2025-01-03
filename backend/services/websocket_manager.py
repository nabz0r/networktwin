import asyncio
import json
from typing import List, Dict
from starlette.websockets import WebSocket

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: Dict):
        for connection in self.active_connections:
            await connection.send_json(message)

    async def broadcast_network_updates(self, network_simulator):
        while True:
            updated_topology = network_simulator.update_topology()
            await self.broadcast(updated_topology.model_dump())
            await asyncio.sleep(5)  # Mise à jour toutes les 5 secondes