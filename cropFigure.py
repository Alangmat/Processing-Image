def cropFigure(width, height, matrix, index_figure):
    fragment = []
    x_list = set()
    y_list = set()

    for y in range(height):
        for x in range(width):
            if matrix[y][x] == index_figure:
                x_list.add(x)
                y_list.add(y)

    minW = min(x_list) - 1 if min(x_list) > 0 else 0
    minH = min(y_list) - 1 if min(y_list) > 0 else 0
    maxW = max(x_list) + 1 if max(x_list) < width - 1 else width - 1
    maxH = max(y_list) + 1 if max(y_list) < height - 1 else height - 1

    for y in range(minH, maxH + 1):
        row = []
        for x in range(minW, maxW + 1):
            if int(matrix[y][x]) == index_figure:
                row.append('*')
            else: row.append('0')
        fragment.append(row)
    
    return fragment