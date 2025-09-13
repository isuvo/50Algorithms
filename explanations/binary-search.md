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
- Imagine looking for a word in a dictionary: you open the book in the middle to see if the word is before or after that page, then keep halving the remaining pages until you find it.
- Speeds up searches in ordered lists like phone books or sorted databases.

## Step-by-step example
- Goal: Find 7 in [1, 3, 5, 7, 9]
- Look at the middle number → 5. Is 7 bigger? Yes, so ignore the left half.
- Now search [7, 9]. Middle is 7 → found it!



