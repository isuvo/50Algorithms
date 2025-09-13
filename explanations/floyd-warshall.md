# Floyd-Warshall 🗺️

## What it does
- Computes shortest paths between all pairs of points.

## How it works
- Like filling a table with city distances and improving it by checking if a stopover city makes trips shorter.

## Step-by-step example
- Start with direct distances between A,B,C
- Try using B as middle: if A→B→C is shorter update the table

## Why it's useful
- Useful for network routing and urban planning.

## Implementation
- [View code](../algorithms/floyd_warshall.py)
