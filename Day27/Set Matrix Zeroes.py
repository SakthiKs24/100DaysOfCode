class Solution(object):
    def setZeroes(self, matrix):
        t = []
        # Step 1: collect zero positions
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    t.append(i)
                    t.append(j)
        # Step 2: process each zero position
        for i in range(0, len(t) - 1, 2):
            for k in range(len(matrix)):
                matrix[k][t[i + 1]] = 0
            matrix[t[i]] = [0] * len(matrix[0])
        return matrix


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix values row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

solution = Solution()
result = solution.setZeroes(matrix)

print("Matrix after setting zeroes:")
for row in result:
    print(row)
