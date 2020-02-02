# -*- coding: utf-8 -*-
"""
Merge sort coding practice

Implement merge sort procedure for sorting an unsorted array

1. Split array into two roughly equal sub-arrays
2. Call mergesort on sub-arrays, recursively dividing (sub-)arrays.
   At smallest array size:
    a. Compare elements of n-sub-arrays to determine placement in
       (n-1)-sub-array
    b. Repeat procedure up the recursion stack
3. Array is now sorted
"""


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2  # find mid-point m of array, floored
        l = arr[:m]
        r = arr[m:]

        # recursively call mergeSort on split sub-arrays
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0  # initialize count for l, r, arr

        '''
        Compare left and right arrays (which have each been sorted recursively)
        to determine smaller element at each position l[i], r[j] to place in
        combined main array arr[k]
        '''
        while k < len(arr):
            # determining element at arr[k]
            if l[i] > r[j]:
                arr[k] = r[j]  # current element at r is placed first in arr
                j += 1
            else:
                arr[k] = l[i]  # current element at l is placed first in arr
                i += 1
            k += 1  # move to determine next position at k

            # catch when either l or r has completed but the other has not
            while i == len(l) and j < len(r):  # l has completed parse
                arr[k] = r[j]
                j += 1
                k += 1
            while j == len(r) and i < len(l):  # r has completed parse
                arr[k] = l[i]
                i += 1
                k += 1
