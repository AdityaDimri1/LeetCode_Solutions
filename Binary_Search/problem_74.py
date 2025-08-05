def searchMatrix(matrix, target: int):
    flat_matrix = []
    for i in range(len(matrix)):
        flat_matrix += matrix[i]
    if target in flat_matrix:
        return True
    else:
        return False
searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)