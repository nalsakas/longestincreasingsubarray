# longestincreasingsubarray
Find longest increasing subarray for any given list

## Problem Statement:
For any given array of integers find the longest subarray, where each element in the subarray is continiously increasing.
Subarray memebers satisfies a[i - 1] < a[i] < a[i + 1] relation for all of its members. If relation doesn't satisfies anymore
 it a signal that current subarray is over, and a new subarray is starting.

Input:
a = [1, 3, 5, 4, 3, 7]
Subarrays are [[1,3,5], [4], [3,7]]

Output:
longest subarray = [1,3,5]
length = 3

## Solution:
Loop through each elements of the list, index i
Start a second loop after each element of the first loop, index j
Advance second loop index j until it hits end of the list or next element is bigger then current element
Calculate distance j - i, for each i
Replace longest distance with current one if it is longer 