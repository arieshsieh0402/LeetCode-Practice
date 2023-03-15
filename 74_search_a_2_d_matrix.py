from typing import List


def search_matrix_brute_force(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        for num in row:
            if num > target:
                return False
            if num == target:
                return True
    return False


def search_matrix_binary_search_1(
        matrix: List[List[int]], target: int
) -> bool:
    if matrix[0][0] > target or matrix[-1][-1] < target:
        return False

    for row in matrix:
        if row[-1] < target:
            continue
        left = 0
        right = len(row)
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


def search_matrix_binary_search_2(
        matrix: List[List[int]], target: int
) -> bool:
    if matrix[0][0] > target or matrix[-1][-1] < target:
        return False

    # Find the index of row
    m_top, m_bot = 0, len(matrix) - 1

    while m_top <= m_bot:
        m_mid = (m_top + m_bot) // 2
        if matrix[m_mid][0] <= target <= matrix[m_mid][-1]:
            break
        elif target > matrix[m_mid][-1]:
            m_top = m_mid + 1
        else:
            m_bot = m_mid - 1

    if m_top > m_bot:
        return False

    # Find the index of column
    n_left, n_right = 0, len(matrix[0]) - 1

    while n_left <= n_right:
        n_mid = (n_left + n_right) // 2
        if matrix[m_mid][n_mid] == target:
            return True
        if target > matrix[m_mid][n_mid]:
            n_left = n_mid + 1
        else:
            n_right = n_mid - 1

    return False
