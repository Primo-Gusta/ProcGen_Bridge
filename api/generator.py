import numpy as np

def generate_cellular_automata(width: int, height: int, seed: int, smoothness: int):
    np.random.seed(seed)
    
    grid = np.random.choice([0, 1], size=(height, width), p=[0.55, 0.45])
    
    for _ in range(smoothness):
        new_grid = grid.copy()
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                neighbors = np.sum(grid[y-1:y+2, x-1:x+2]) - grid[y, x]
                
                if neighbors > 4:
                    new_grid[y, x] = 1
                elif neighbors < 4:
                    new_grid[y, x] = 0
            grid = new_grid
            
        return grid.tolist()