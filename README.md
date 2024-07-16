# Python Divide-And-Conquer Sorting Algorithm (DAC)

## Overview
The Divide and Conquer Sorting Algorithm (DAC) is a custom implementation of a sorting algorithm based on the divide-and-conquer approach. This algorithm recursively divides an input array into smaller subarrays, sorts these subarrays, and then merges them to produce a sorted array.

## Functionality
- **Input**: An unsorted array of numerical values.
- **Output**: A sorted array of numerical values.

## How It Works
1. **Dividing the Array**:
   - The algorithm splits the input array into two halves.
   - If the array has an odd number of elements, the extra element is included in the second half.

2. **Recursive Sorting**:
   - The algorithm recursively calls itself to sort the two halves.
   - This continues until the subarrays contain only one element each, which are inherently sorted.

3. **Merging Subarrays**:
   - The sorted subarrays are then merged together.
   - During merging, elements from the two subarrays are compared and arranged in ascending order.
   - Special handling ensures elements are correctly positioned to maintain order.

4. **Key Mechanism**:
   - A boolean key is used to indicate whether the merging phase should start.

## Example
Given an array, the DAC algorithm will produce a sorted array. For instance, the array `[78, 12, 89, 34, 2, 789, 1, 3, 5, 12, 555, 6]` will be sorted into `[1, 2, 3, 5, 6, 12, 12, 34, 78, 89, 555, 789]`.

## Usage
To use this algorithm, call the `rct` function with your unsorted array as the argument. The function returns the sorted array.

## Summary
This project demonstrates a practical application of the divide-and-conquer paradigm, providing an efficient way to sort arrays through recursion and merging.
