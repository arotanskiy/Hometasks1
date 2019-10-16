"""
These are the hometask solutions from PY10019 practice
"""
import random
from time import sleep
from statistics import mean

duration = 10
# This function generates a list of 20 integers.
def list_generator():
    temp_list = [random.randint(-10, 10) for _ in range(20)]
    print("\nUsed random list of integers:\n", temp_list)
    return temp_list

def list_generator2():
    temp_list = []
    for i in range(20):
        temp_list.append(random.randint(-10, 10))
    print("\nUsed random list of integers:\n", task2_list)
    return temp_list

# Task 1
def task1():
    """
    Task: There is a list of integers. Need to count a number of even integers.
    """
    task1_list = list_generator()
    count = 0
    for elm in task1_list:
        if elm % 2 == 0:
            count += 1
    print("\nNumber of even integers is a list is: {}".format(count))

# Task 2
def task2():
    """
    Task: There is a list of integers. Need to replace fifth element of a list on a arithmetic mean of all list
    """
    task2_list = list_generator()
    calc = mean(task2_list)
    task2_list[5] = calc  # assuming fifth element means list's index (starting from 0)
    print("Modified random list of integers:\n", task2_list)

# Task 3
def task3():
    """
    Task: There is a list of integers. Need to exchange first and max elements.
    """
    task3_list = list_generator()
    max = len(task3_list) - 1
    task3_list[1], task3_list[max] = task3_list[max], task3_list[1]
    print("Modified random list of integers:\n", task3_list)

# Task 4
def task4():
    """
    Task: There is a list of integers. Need to compare the numbers of odd and even and chose the highest.
    """
    task4_list = list_generator()
    count_even = 0
    for elm in task4_list:
        if elm % 2 == 0:
            count_even += 1
    if count_even > (len(task4_list) / 2):
        print("\nNumber of even more than odd and is: {}".format(count_even))
    else:
        print("\nNumber of odd more than even and is: {}".format((len(task4_list) - count_even)))

# Task 5
def task5():
    """
    Task: There is a list of integers. Need to count a number elements what are greater than first element
    """
    task5_list = list_generator()
    count = 0
    for elm in range (len(task5_list)):
        if task5_list[elm] > task5_list[1]:
            count += 1
    print("\nNumber of elements what are greater then first one: ", count)

# Task 6
def task6():
    """
    Task: There is a list of integers. Need to find indexes of min and max elements.
    """
    task6_list = list_generator2()
    elm = 1
    max_idx = []
    min_idx = []
    min_value = task6_list[0]
    max_value = task6_list[0]
    while elm < (len(task6_list)):
        if task6_list[elm] > max_value:
            max_value = task6_list[elm]
            max_idx.clear()
            max_idx.insert(0, elm)
        elif task6_list[elm] == max_value:
            max_idx.append(elm)
        elif task6_list[elm] < min_value:
            min_value = task6_list[elm]
            min_idx.clear()
            min_idx.insert(0, elm)
        elif task6_list[elm] == min_value:
            min_idx.append(elm)
        elm += 1
    print("\nMin index is: ", min_idx, end='    ')
    print("Min value is: ", min_value)
    print("\nMax index is: ", max_idx, end='    ')
    print("Max value is: ", max_value)

# Task 7
def task7():
    """
    Task: There is a list of integers. Need to create a new list where elements are calculated by deduction
    from an original element and arithmetic mean of all elements
    """
    task7_list = list_generator()
    avg = mean(task7_list)
    task7_list = [round((i - avg), 2) for i in task7_list]
    print("\nArithmetic mean is:  ", avg)
    print("\nDeducted by arithmetic mean list is:\n", task7_list)

# Task 8
def task8():
    """
    Task: There is a list of integers. Need to count a number and sum of positive even elements
    """
    task8_list = list_generator()
    mod_list = []
    for elm in range(len(task8_list)):
        if task8_list[elm] >= 0 and task8_list[elm] %2 == 0:
            mod_list.append(task8_list[elm])
    sum_ = sum(mod_list)
    num_ = len(mod_list)
    print("\nNumber of positive even elements is:  ", num_, "\nSum of positive even elements is:  ", sum_)

# Task 9
def task9():
    """
    Task:  There is a list of integers. Need to to calculate sum and difference of min and max elements
    """
    task9_list = list_generator()
    sum_ = max(task9_list) + min(task9_list)
    diff_ = max(task9_list) - min(task9_list)
    print("\nSum of max and min elements of a list is:   ", sum_, "\nDifference of max and min elemets is:   ", diff_)


# Task 10
def task10():
    """
    Task: There is a list of integers. Need to replace elements divided by 3 on a sum of odd elements
    """
    task10_list = list_generator()
    sum_odd = 0
    for elm in range(len(task10_list)):
        if task10_list[elm] % 2 == 1:
            sum_odd = sum_odd + task10_list[elm]
    for elm in range(len(task10_list)):
        if task10_list[elm] % 3 == 0:
            task10_list[elm] = sum_odd
    print("\nSum of all odd elemetns is:  ", sum_odd, "\nList with replaced elements by sum is:   ", task10_list)


tasks_list = [("task" + str(tid)) for tid in range(1,11)]
print("\n Specify an hometask item in a range from 1 to 10:\n")
try:
    tid = input()
    if tid.isdigit() == False:
        print("\n Input is not digit. Bye!  ")
        exit(1)
except (ValueError, TypeError):
    print("\n Value is not valid. Bye! ")
    exit(1)
except Exception:
    print("\n Something was going wrong. Bye! ")
    exit(1)
tid = int(tid) - 1
help(eval(tasks_list[tid]))
eval(tasks_list[tid])()

