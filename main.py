from processingFigure import cropFigure, checkCell
from PIL import Image
import numpy as np
from math import inf, sqrt

# Площадь фигуры по индексу
def SFigure(width, height, matrix, index_figure):
    s = 0
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == index_figure:
                s += index_figure
    if index_figure > 0:
        return (s / index_figure)
    else:
        return 0

# Центр масс фигуры по индексу (точный метод)
def CenterOfMassAccurate(width, height, matrix, index_figure):
    x_list = []
    y_list = []
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == index_figure:
                x_list.append(x)
                y_list.append(y)
    X = sum(x_list) / len(x_list)
    Y = sum(y_list) / len(y_list)
    return (round(X,2),round(Y,2))

# Центр масс фигуры по индексу (быстрый метод)
def CenterOfMassSpeed(width, height, matrix, index_figure):
    x_list = set()
    y_list = set()
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == index_figure:
                x_list.add(x)
                y_list.add(y)
    X = sum(x_list) / len(x_list)
    Y = sum(y_list) / len(y_list)
    return (round(X,2),round(Y,2))

# Периметр фигуры по индексу (быстрый метод)
def PerimeterInaccurate(width, height, matrix, index_figure):
    fragmentWithFigure = cropFigure(width, height, matrix, index_figure)
    perimetr = 0
    for y in range(1, len(fragmentWithFigure) - 1):
        for x in range(1, len(fragmentWithFigure[y]) - 1):
            if fragmentWithFigure[y][x] == '*':
                if fragmentWithFigure[y - 1][x] == 0:
                    perimetr += 1
                if fragmentWithFigure[y + 1][x] == 0:
                    perimetr += 1
                if fragmentWithFigure[y][x - 1] == 0:
                    perimetr += 1
                if fragmentWithFigure[y][x + 1] == 0:
                    perimetr += 1
    return perimetr

# Периметр фигуры по индексу (точный метод)
def PerimeterAccurate(width, height, matrix, index_figure):
    fragmentWithFigure = cropFigure(width, height, matrix, index_figure)
    perimetr = 0
    m = 0
    for y in range(1, len(fragmentWithFigure) - 1):
        for x in range(1, len(fragmentWithFigure[y]) - 1):
            if fragmentWithFigure[y][x] == '*':
                if fragmentWithFigure[y - 1][x] != '*':
                    fragmentWithFigure[y - 1][x] += 1
                if fragmentWithFigure[y + 1][x] != '*':
                    fragmentWithFigure[y + 1][x] += 1
                if fragmentWithFigure[y][x - 1] != '*':
                    fragmentWithFigure[y][x - 1] += 1
                if fragmentWithFigure[y][x + 1] != '*':
                    fragmentWithFigure[y][x + 1] += 1
    for y in range(len(fragmentWithFigure)):
        for x in range(len(fragmentWithFigure[y])):
            if fragmentWithFigure[y][x] != '*':
                if fragmentWithFigure[y][x] == 2:
                    m += 1
                else:
                    perimetr += fragmentWithFigure[y][x]
    perimetr = perimetr + m * sqrt(2)
    return perimetr

def coefficientRoundness(s, p):
    return p**2 / s
    

# ####################################################
# ############## Основной блок кода ##################
# ####################################################
image = Image.open('input.png').convert('L')
image_array = np.array(image)
binary_matrix = (image_array < 128).astype(int)

height = len(binary_matrix)
width = len(binary_matrix[0])

print(height, width)

counter = 1

# ####################################################
# ############## Маркировка рекурсия  ################
# ####################################################

for i in range(height):
    for j in range(width):
        if binary_matrix[i][j] == 1:
            counter += 1
            checkCell(width, height, j, i, binary_matrix, counter)


# ####################################################
# ############## Маркировка построчно ################
# ####################################################

# def rowCheckCell(j, i, binary_matrix, arr):
#     global counter
#     leftCell = binary_matrix[i][j - 1]
#     topCell = binary_matrix[i - 1][j]
#     if topCell != 0:
#         binary_matrix[i][j] = topCell
#         if leftCell != 0 and leftCell != topCell and int(leftCell) not in arr[topCell - 1]:
#             arr[topCell - 1].append(int(leftCell))
#     elif leftCell != 0:
#         binary_matrix[i][j] = leftCell
#     else:
#         counter += 1
#         binary_matrix[i][j] = counter
#         arr.append([counter])
    
# def swapValue(arr, value, newValue):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] == value:
#                 arr[i][j] = newValue
#                 if j > 0:
#                     if arr[i][j - 1] == arr[i][j]:
#                         arr[i].pop(j)

# def finishMarking(binary_matrix, arr):
#     global counter
#     for current_value in range(counter, 1, -1):
#         print("=====================")
#         print(current_value)
#         print(arr)
#         print(binary_matrix)
#         for j in range(len(arr) - 1, 0, -1):
#             if isinstance(arr[j], list):
#                 if len(arr[j]) == 1:
#                     arr.pop(j)
#                     continue
#                 for k in range(len(arr[j]) - 1, 0, -1):
#                     if arr[j][k] == current_value and arr[j][k] != arr[j][k-1]:
#                         new_value = arr[j][k-1]
#                         swapValue(arr, current_value, new_value)
#                         binary_matrix[binary_matrix == current_value] = new_value

# arr = [[1]]
# for i in range(1, height - 1):
#     for j in range(1, width - 1):
#         if binary_matrix[i][j] == 1:
#             rowCheckCell(j,i, binary_matrix, arr)
# finishMarking(binary_matrix, arr)

# print(binary_matrix)
# print(f'Кол-во фигур {counter - 1}')

for s in range(2, counter + 1):
    if s in binary_matrix:
        sFig = SFigure(width, height, binary_matrix, s)
        pFig = PerimeterAccurate(width, height, binary_matrix, s)
        print("==============================")
        print(f'Индекс фигуры: {s}')
        print(f'Площадь фигуры: {sFig}')
        print(f'Центр масс фигуры (точный подход): {CenterOfMassAccurate(width, height, binary_matrix, s)}')
        print(f'Центр масс фигуры (быстрый подход): {CenterOfMassSpeed(width, height, binary_matrix, s)}')
        print(f'Периметр фигуры (быстрый способ): {PerimeterInaccurate(width, height, binary_matrix, s)}')
        print(f'Периметр фигуры (точный способ): {pFig}')
        print(f'Коэффициент округлости: {coefficientRoundness(sFig, pFig)}')


