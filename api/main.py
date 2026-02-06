from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from generator import generate_cellular_automata

PORT = int(os.environ.get("PORT", 10000))

app = FastAPI(
    title="ProcGen-Bridge API",
    description="Backend engine for procedural map generation in Godot 4.5",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/generate")
async def generate_map(
    width: int = Query(50, gt=0, lt=500),
    height: int = Query(50, gt=0, lt=500),
    seed: int = 42,
    smoothness: int = Query(4, ge=1, le=50),
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
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=False)