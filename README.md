# 🌲 GridWeaver: Procedural Biome Generator for Godot 4.5

**GridWeaver** is a powerful productivity tool for Godot developers. It allows you to generate organic, complex tile-based maps—like forests, clearings, and caves—directly within the Godot Editor with a single click. By leveraging a dedicated generation engine, it creates natural-looking biomes that would take hours to paint manually.

## ✨ Core Functionalities

- **Instant Editor Preview**: No need to run your game. Adjust parameters and see the results instantly on your `TileMapLayer` in the 2D Viewport.
- **Organic Biome Algorithms**: Uses advanced **Cellular Automata** to move beyond simple random noise, creating clusters and paths that feel natural.
- **Customizable Generation**:
    - **Width & Height**: Control the scale of the generated area.
    - **Smoothness**: Define the "density" of your biome (from scattered trees to thick, impenetrable forests).
    - **Seed System**: Lock a specific layout or explore infinite variations by changing the seed.
- **Native Integration**: Works directly with Godot's built-in `TileSet` and `TileMapLayer` systems.

## 🚀 How It Works (The User Experience)

1.  **Select Your Layer**: Click on any `TileMapLayer` in your Scene Tree.
2.  **Configure**: Open the **GridWeaver Dock** and set your desired forest density and map size.
3.  **Generate**: Click **"Generate Map in Editor"**.
4.  **Refine**: Change the smoothness or seed and regenerate until you find the perfect layout for your level design.

## 🛠️ Installation

1.  Download this repository.
2.  Move the `addons/gridweaver` folder into your project's `addons/` directory.
3.  Enable the plugin in **Project Settings > Plugins**.

## 🔮 Future Implementations

- Enable random generation of seeds 
- UndoRedo system
- Better server response
---
*Developed by **Gustavo** — Enhancing level design workflows for Godot 4.5.*
