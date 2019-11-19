import numpy as np
import math
import ctypes
from graphics import *
# from array import array

# Input of play field size
n = 7
# Temp list generator
battle_field = np.array(['' for x in range(n * n)]).reshape(n, n)
# battle_field = np.arange(n * n).reshape(n, n)
# for x in battle_field:
#     print(*x)
# s = 10
# for k in range(n):
#     battle_field[k][k] = s
#     s += 1

def parce_step(coord_x, coord_y, step, battle_field):
#    coord_x = 6
#    coord_y = 6
    if step == 'X':
        battle_field[coord_y][coord_x] = 1
    else:
        battle_field[coord_y][coord_x] = 0
    # for x in battle_field:
    #     print(*x)

    # Check coordinates are not less or more available
    if (coord_x - 2) < 0:
        x_min = 0
        x_max = coord_x + 3
        area_x = coord_x
    elif (coord_x + 3) > n:
        x_min = coord_x - 2
        x_max = n
        area_x = 2
    else:
        x_min = coord_x - 2
        x_max = coord_x + 3
        area_x = 2

    if (coord_y - 2) < 0:
        y_min = 0
        y_max = coord_y + 3
        area_y = coord_y
    elif (coord_y + 3) > n:
        y_min = coord_y - 2
        y_max = n
        area_y = 2
    else:
        y_min = coord_y - 2
        y_max = coord_y + 3
        area_y = 2

    # Area for analyzing
    area = battle_field[y_min:y_max, x_min:x_max]
    # for x in area:
    #     print(*x)
    return area_y, area_x, area

def chose_variants(coord_x, coord_y, step, battle_field):
    area_y, area_x, area = parce_step(coord_x, coord_y, step, battle_field)

    dr = np.diagonal(area, offset=(area_x - area_y))  # right diagonal of area
    # print('right: ', [i.tolist() for i in dr])
    # print(*dr)
    dl = np.fliplr(area).diagonal(offset=(len(area[area_x]) - 1 - area_x - area_y))  # left diagonal of area
    # print('left: ', [i.tolist() for i in dl])
    h = area[area_y]  # horizontal line of area
    # print('horiz: ', [i.tolist() for i in h])
    # print(*h)
    v = area[:, area_x]  # vertical line of area
    # print('vert: ', [i.tolist() for i in v])
    # print(dr, dl, h, v)
    for i in (dr, dl, h, v):
        if analyze(i, step):
            print('Win')
            return True


def analyze(var, step):
    win_list = []
    if step == 'X':
        tmp = '1'
    else:
        tmp = '0'
    for count in range(len(var)):
        if var[count] == tmp:
            win_list.append([1])
            if len(win_list) == 3:
                return True
        else:
            win_list = []


def Board(window):
    # window.setBackground("black")
    rectangle = Rectangle(Point(0, 0), Point(n, n))
    rectangle.setFill("white")
    rectangle.draw(window)

    for i in range(0, n):
        Line(Point(0, i), Point(n, i)).draw(window)
    for x in range(0, n + 1):
        Line(Point(x, 0), Point(x, n)).draw(window)

step = 'X'
win = GraphWin("Game field", 400, 400)
win.setCoords(0, 0, n, n)
Board(win)
while True:
    point = win.getMouse()
    coord_x = math.floor(point.getX())
    coord_y = n - 1 - math.floor(point.getY())
    # print(coord_x, coord_y)
    if step == 'X':
        obj = Text(Point(math.floor(point.getX()) + 0.5, math.floor(point.getY()) + 0.5), step)
        obj.setSize(30)
        obj.setTextColor("red")
        obj.draw(win)
        if chose_variants(coord_x, coord_y, step, battle_field):
            if ctypes.windll.user32.MessageBoxW(0, 'Winner is: X', 'Congragulations!!!', 0):
                break
        step = '0'
    else:
        obj = Text(Point(math.floor(point.getX()) + 0.5, math.floor(point.getY()) + 0.5), step)
        obj.setSize(30)
        obj.setTextColor("cyan")
        obj.draw(win)
        if chose_variants(coord_x, coord_y, step, battle_field):
            if ctypes.windll.user32.MessageBoxW(0, 'Winner is : 0', 'Congragulations!!!', 0):
                break
        step = 'X'

win.close()

# chose_variants()
