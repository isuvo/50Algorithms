# Merge Sort 🪄

## What it does
- Sorts a list by splitting it into halves and merging them in order.

## How it works
- Like dividing a deck of cards into small piles, sorting each, then combining them.

## Step-by-step example
- Start with [4, 2, 3, 1]
- Split into [4,2] and [3,1]
- Split again: [4],[2] and [3],[1]
- Merge [4] + [2] → [2,4]; [3] + [1] → [1,3]
- Merge [2,4] + [1,3] → [1,2,3,4]

## Why it's useful
- Great for sorting big data sets efficiently.

## Implementation
- [View code](../algorithms/merge_sort.py)
