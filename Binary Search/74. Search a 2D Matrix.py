def searchMatrix(matrix, target):
    Rows, Cols = len(matrix), len(matrix[0])
    top, btm = 0, Rows-1
    while top <= btm:
        mid = (top+btm)//2
        if target < matrix[mid][0]:
            btm = mid-1
        elif target > matrix[mid][-1]:
            top = mid+1
        else:
            break

    if btm < top:
        return False

    l, r = 0, Cols-1

    while l <= r:
        m_row = (l+r)//2
        if target < matrix[mid][m_row]:
            r = m_row-1
        elif target > matrix[mid][m_row]:
            l = m_row+1
        else:
            return True
    return False
