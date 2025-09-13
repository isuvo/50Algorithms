# Bellman-Ford 🚌

## What it does
- Finds shortest paths even if some roads have negative tolls.

## How it works
- Like recalculating bus fares over several rounds to catch cheaper deals.

## Step-by-step example
- Edges: A→B cost 4, A→C cost 5, C→B cost -2
- First pass: B=4 via A→B, second pass: B=3 via A→C→B

## Why it's useful
- Detects negative cycles and handles varying costs.
