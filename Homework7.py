"""
These are the solutions from PY10019 practice 7_loop_and_dict homework
"""
import random
from time import sleep
from statistics import mean
from array import array
import numpy as np

NAME = "Alex Rotanskiy"
COLLABORATORS = "Student"

def array_gen(n):
    """
    This is an array n x n elements generator. Random values are in a range from -10 to 10
    :return: array n x n elements
    """
    arr = np.random.randint(-10, 10, n * n).reshape(n, n)
#    arr = np.random.rand(n, n)
    print("\nUsed array with size N x N and N = {}:\n{}".format(n, arr))
    return (arr)

def task1(n):
    """
    Need to calculate a sum of elements the last column of array
    :return:
    """
    task1_arr = array_gen(n)
    sum = 0
    for i in range(n):
        sum += task1_arr[i, n - 1]
    print("\nSum of the elements of last column is: ", sum)
    # raise NotImplementedError()

def task2(n):
    """
    Need to calculate a result of multiplication of the first row elements
    :return:
    """
    task2_arr = array_gen(n)
    mult = 1
    for i in range(n):
        mult *= task2_arr[1, i]
    print("\nMultiplication of the first row elements is: ", mult)
    # raise NotImplementedError()

def task3(n):
    """
    Need to calculate a sum of each row
    :return:
    """
    n = 10
    task3_arr = array_gen(n)
    for i in range(n):
        sum_ = 0
        for j in range(n):
            sum_ += task3_arr[i, j]
        print("Sum of the {} row elements is: {}".format(i, sum_))
    # raise NotImplementedError()

def task4(n):
    """
    Need to replace each element which is lower than arithmetical mean of all elements to 0 (zero)
    :return:
    """
    task4_arr = array_gen(n)
    # calculate an arithmetical mean of all array elements
    arth = 0
    sum_ = 0
    for i in range(n):
        for j in range(n):
            sum_ += task4_arr[i, j]
    size = n * n
    arth = round(sum_ / size)
    print("\nSum of elements is: {}".format(sum_))
    print("Size of array is: {}".format(size))
    print("Arithmetical mean of all elements is: {}".format(arth))
    # replacing the elements
    for i in range(n):
        for j in range(n):
            if task4_arr[i, j] < arth:
                task4_arr[i, j] = 0
    print("Array after replacing:\n", task4_arr)
    # raise NotImplementedError()

def task5(n):
    """
    Array 3 x 4. Need to exchange the lowest elements in 1 and 3 rows
    :return:
    """
    n = 3
    m = 4
    task5_arr = np.random.randint(-10, 10, n * m).reshape(n, m)
    print("Original array is:\n", task5_arr)
    # specify the rows where elements shall be replaced
    target = [0, 2]
    # find two candidates for min elements
    for i in target:
        if task5_arr[i][0] < task5_arr[i][1]:
            min1 = 0
            min2 = 1
        else:
            min1 = 1
            min2 = 0
        # find indexes of the lowest elements
        for k in range(2, m):
            if task5_arr[i][k] < task5_arr[i][min1]:
                temp = min1
                min1 = k
                if task5_arr[i][temp] < task5_arr[i][min2]:
                    min2 = temp
            elif task5_arr[i][k] < task5_arr[i][min2]:
                min2 = k
    # what should we do if there are two same elements???
        print("\nThe lowest values for a {} row is: {} and {}".format(i, task5_arr[i][min1], task5_arr[i][min2]))
        # replace elements
        task5_arr[i][min1], task5_arr[i][min2] = task5_arr[i][min2], task5_arr[i][min1]
    print("\nModified array is:\n", task5_arr)
    # raise NotImplementedError()
task5(3)