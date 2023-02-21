def get_row(row_index: int):
    num_rows = row_index + 1
    pascals_triangle = []
    for i in range(num_rows):
        pascals_triangle.append([1] * (i + 1))
        for j in range(1, i):
            pascals_triangle[i][j] = (
                pascals_triangle[i - 1][j - 1] +
                pascals_triangle[i - 1][j]
            )
    return pascals_triangle[row_index]


def get_row_renew(row_index):
    if row_index == 0:
        return [1]
    ans = [1, 1]
    for _ in range(1, row_index):
        temp = [1]
        for i in range(len(ans) - 1):
            temp.append(ans[i] + ans[i + 1])
        temp.append(1)
        ans = temp
    return ans
