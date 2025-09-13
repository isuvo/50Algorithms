# Binary Search 🔍

## What it does
- Finds a specific item in a sorted list by repeatedly cutting the list in half.

## How it works
- Like looking up a word in a dictionary by opening near the middle and deciding which half to keep.

## Step-by-step example
- Look for 7 in [1, 3, 5, 7, 9]
- Middle is 5 → too small, keep right half
- Now list [7, 9]; middle is 7 → found!

## Why it's useful
- Quickly searches large sorted lists like phone directories.

## Implementation
- [View code](../algorithms/binary_search.py)
