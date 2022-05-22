def convert_to_title(column_number: int) -> str:
    """
    Given an integer columnNumber,
    return its corresponding column title as it appears in an Excel sheet.
    """
    char = [chr(w).upper() for w in range(ord('a'), ord('z') + 1)]
    result = []

    while column_number > 0:
        result.append(char[(column_number - 1) % 26])
        column_number = (column_number - 1) // 26

    result.reverse()

    return ''.join(result)
