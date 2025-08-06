class Solution(object):
    def spiralOrder(self, matrix):
        result = []  # Final spiral output

        if not matrix:
            return result  # Return empty if input is empty

        top, bottom = 0, len(matrix) - 1        # Row boundaries
        left, right = 0, len(matrix[0]) - 1     # Column boundaries

        while top <= bottom and left <= right:
            # Left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right to left (only if top still <= bottom)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to top (only if left still <= right)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix row by row (space-separated):")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
    while len(row) != cols:
        print(f"❌ Please enter exactly {cols} values.")
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
    matrix.append(row)

sol = Solution()
spiral = sol.spiralOrder(matrix)

print("Spiral Order:", spiral)
