class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr, target):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l + r)//2
                if arr[mid] == target:
                    return True 
                if arr[mid] > target:
                    r = mid - 1
                else: 
                    l = mid + 1
            return False 

        for j in matrix:
            if binarySearch(j, target):
                return True
        return False 
        # Time: O(mlogn)
        # Space: O(1)
