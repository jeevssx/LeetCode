class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for matri in matrix:
            if target >= matri[0] and target <= matri[len(matri) - 1]:
                left = 0
                right = len(matri) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if target > matri[mid]:
                        left = mid + 1
                    if target < matri[mid]:
                        right = mid - 1
                    if matri[mid] == target:
                        return True
        return False
                        