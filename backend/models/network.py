from pydantic import BaseModel, Field
from typing import List, Optional

class Node(BaseModel):
    id: str
    name: str
    type: str = 'default'
    bandwidth: float = 0.0
    latency: float = 0.0
    reliability: float = 1.0

class NetworkTopology(BaseModel):
    nodes: List[Node] = []
    links: List[dict] = []
    timestamp: Optional[float] = None