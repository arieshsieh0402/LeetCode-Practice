def generate(num_rows: int):
    pascals_triangle = []
    for i in range(num_rows):
        pascals_triangle.append([1] * (i + 1))
        for j in range(1, i):
            pascals_triangle[i][j] = (
                pascals_triangle[i - 1][j - 1] +
                pascals_triangle[i - 1][j]
            )
    return pascals_triangle
