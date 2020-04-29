"""Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum=min(abs(arr[i]-arr[i-1]) for i in range (1, len(arr)))
        results=[[arr[i-1], arr[i]] for i in range (1, len(arr)) if arr[i] - arr[i-1] == minimum]
                
        return results

"""I also learnt about a zip function that can be used in Python to map the similar index of multiple containers.
The code is a lot cleaner with zip"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]  
