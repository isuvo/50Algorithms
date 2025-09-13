# Binary Search 🔍

## What it does
- Finds a specific item in a sorted list by repeatedly cutting the list in half.

## How it works
- Imagine looking for a word in a dictionary: you open the book in the middle to see if the word is before or after that page, then keep halving the remaining pages until you find it.

## Step-by-step example
- Goal: Find 7 in [1, 3, 5, 7, 9]
- Look at the middle number → 5. Is 7 bigger? Yes, so ignore the left half.
- Now search [7, 9]. Middle is 7 → found it!

## Why it's useful
- Speeds up searches in ordered lists like phone books or sorted databases.
