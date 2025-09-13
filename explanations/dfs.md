# Depth-First Search 🌳

## What it does
- Explores as far as possible down one path before backtracking.

## How it works
- Like walking through a maze, taking one path until a dead end then backtracking.

## Step-by-step example
- Maze rooms: A-B, A-C, B-D
- Start A→B→D, back to B, back to A, then to C
- Visited order: A, B, D, C

## Why it's useful
- Useful for exploring puzzles or file systems.
- Helps in solving puzzles and exploring networks like social connections or file systems.
- Explores every branch of a network or tree by going as far as possible before backtracking.

## How it works
- Imagine walking through a maze: you pick a path and keep going until you hit a dead end, then go back to try a different path.

## Step-by-step example
- Maze rooms: A connects to B and C; B connects to D
- Start at A → go to B → go to D (no more rooms) → back to B → back to A → go to C
- Visited order: A, B, D, C

