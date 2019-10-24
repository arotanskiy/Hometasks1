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

def task6(n):
    """
    Array 10x10. Need to find a min element in a main diagonal
    :return:
    """
    task6_arr = array_gen(n)
    min_elm = task6_arr[0, 0]
    print("\nThe main diagonal is: ", end="")
    for i, j in zip(range(8), range(8)):
        print(task6_arr[i, j], end=" ")
        if task6_arr[i, j] < min_elm:
            min_elm = task6_arr[i, j]
        i += 1
        j += 1
    print("\nMin element in a main diagonal is: {}".format(min_elm))


def task7(limit=100):
    """
    Need to find first 100 simple numbers
    :return:
    """
    task7_list = []
    count = 0
    num = 2
    while count < limit:
        value = 2
        while num >= value:
            if (num % value) == 0 and (num != value):
                break
            elif (num % value) == 0 and (num // value) == 1:
                task7_list.append(num)
                count += 1
            value += 1
        num += 1
    print("\nFirst {} simple numbers are {}".format(limit, task7_list))


def task8():
    """
    Total number is 740 animals with 1980 paws. Krol has 4 paws, phaz has 2 paws. Need to find amount of krol and phaz.
    :return:
    """
    total_amount = 740
    total_paw = 1980
    krol_paw = 4
    phaz_paw = 2
    for i in range(int(total_paw / krol_paw)):
        for j in range(int(total_paw / phaz_paw)):
            if (i * krol_paw) + (j * phaz_paw) == total_amount:
                print("Number of Krol is {} and Phaz is {}".format(i, j))


def task9(A, N):
    """
    Raise a number A to a power N
    :return: A in power N
    """
    return pow(A, N)

# print(task9(3, 5))


def task10(A):
    """
    Check if a number A is result of a power 3
    :return: A in power N
    """
    pow = 3
    x = 1
    while x ** pow <= A:
        if x ** pow == A:
            print("Number {} is a power of 3".format(A))
            exit(0)
        else:
            x += 1
    print("Number {} is NOT a power of 3".format(A))

# task10(27)


def task11(n):
    """
    Check if a Syracuse hypothesis is correct.
    :return: True or False
    """
    result = False
    tmp = n
    while n >= 1:
        if (n % 2) == 0:
            n = n / 2
            if n == 1:
                print("Syracuse hypothesis is correct for {}".format(tmp))
                result = True
                break
        if (n % 2) == 1:
            n = (n * 3 + 1) / 2
            if n == 1:
                print("Syracuse hypothesis is correct for {}".format(tmp))
                result = True
                break
    return result

task11(6)