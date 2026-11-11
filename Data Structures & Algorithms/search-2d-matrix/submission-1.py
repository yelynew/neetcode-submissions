class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for x in range(m):
            if target > matrix[x][-1]:
                continue
            else:
                if target in matrix[x]:
                    return True
                else:
                    return False
        return False

        