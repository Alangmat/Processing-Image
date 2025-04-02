from cropFigure import cropFigure
from PIL import Image
import numpy as np
from math import inf, sqrt


# Маркировка фигур
def CheckCell(width, height, x, y, matrix, c):
    if matrix[y][x] == 1:
        matrix[y][x] = c
        if x + 1 < width:
            CheckCell(width, height, x + 1, y, matrix, c)
        if y + 1 < height:
            CheckCell(width, height, x, y + 1, matrix, c)
        if x - 1 >= 0:
            CheckCell(width, height, x - 1, y, matrix, c)
        if y - 1 >= 0:
            CheckCell(width, height, x, y - 1, matrix, c) 

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

    
    

image = Image.open('input.png').convert('L')
image_array = np.array(image)
binary_matrix = (image_array < 128).astype(int)

# print(binary_matrix)

height = len(binary_matrix)
width = len(binary_matrix[0])

print(height, width)

counter = 1

for i in range(height):
    for j in range(width):
        if binary_matrix[i][j] == 1:
            counter += 1
            CheckCell(width, height, j, i, binary_matrix, counter)

print(f'Кол-во фигур {counter - 1}')

for s in range(2, counter + 1):
    print("==============================")
    print(f'Индекс фигуры: {s}')
    print(f'Площадь фигуры: {SFigure(width, height, binary_matrix, s)}')
    print(f'Центр масс фигуры (точный подход): {CenterOfMassAccurate(width, height, binary_matrix, s)}')
    print(f'Центр масс фигуры (быстрый подход): {CenterOfMassSpeed(width, height, binary_matrix, s)}')
    print(f'Периметр фигуры (быстрый способ): {PerimeterInaccurate(width, height, binary_matrix, s)}')
    print(f'Периметр фигуры (точный способ): {PerimeterAccurate(width, height, binary_matrix, s)}')

# fragment = cropFigure(width, height, binary_matrix, 3)
# for i in range(len(fragment)):
#     print(fragment[i])
