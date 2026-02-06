from fastapi import FastAPI, Query
import uvicorn
from generator import generate_cellular_automata

SERVER_CONFIG = {
    "app": "main:app",
    "host": "0.0.0.0",
    "port": 8000,
    "reload": True,
    "log_level": "info"
}

app = FastAPI(
    title="ProcGen-Bridge API",
    description="Backend engine for procedural map generation in Godot 4.5",
    version="1.0.0"
)

@app.get("/generate")
async def generate_map(
    width: int = Query(50, gt=0, lt=5000),
    height: int = Query(50, gt=0, lt=5000),
    seed: int = 42,
    smoothness: int = 4,
):
    map_data = generate_cellular_automata(width, height, seed, smoothness)
    return{
        "metadata":{
            "width": width,
            "height": height,
            "seed": seed,
        },
        "map": map_data
    }
    
if __name__ == "__main__":
    uvicorn.run(**SERVER_CONFIG)