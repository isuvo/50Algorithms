# Boyer-Moore 🕵️

## What it does
- Searches from the end of the pattern and skips ahead when letters don’t match.

## How it works
- Like comparing the last letter of a word first to quickly rule out mismatches.

## Step-by-step example
- Text "here is a test" pattern "test"
- Mismatch t vs r allows skipping several letters

## Why it's useful
- Very fast for long texts.

## Implementation
- [View code](../algorithms/boyer_moore.py)
