import numpy as np
from array import array

# Input of play field size
n = 7
# Temp list generator
# battle_field = np.array(['' for x in range(n * n)]).reshape(n, n)
battle_field = np.arange(n * n).reshape(n, n)
# for x in battle_field:
#     print(*x)
s = 0
for k in range(n):
    battle_field[k][k] = s
    s += 1

def parce_step(*args):
    coord_x = 0
    coord_y = 0
    battle_field[coord_y][coord_x] = 100
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
    for x in area:
        print(*x)
    return area_y, area_x, coord_x, coord_y, area

def analyzing():
    area_y, area_x, coord_x, coord_y, area = parce_step(battle_field)
    # diags_right = [area[::1, :].diagonal(i) for i in range(-area.shape[1]+3, area.shape[0]-2)]
    # print([i.tolist() for i in diags_right])
    # diags_left = [area[::-1, :].diagonal(i) for i in range(-area.shape[0]+3, area.shape[1]-2)]
    # print([i.tolist() for i in diags_left])

    # diag_right = [np.diagonal(area, offset=(area_x - area_y))]
    # print([i.tolist() for i in diag_right])
    diag_left = [np.fliplr(area).diagonal(offset=((area_x - 0) - area_y))]
    print([i.tolist() for i in diag_left])

    horizontal = [area[area_x]]
    # diag_left = [np.diagonal(area[::-1, :], offset=(area_x - area_y))]
    # print([i.tolist() for i in horizontal])
    vertical = [area[:, area_y]]
    # print([i.tolist() for i in vertical])
analyzing()
