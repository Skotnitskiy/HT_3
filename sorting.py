from random import randint
import random
import datetime


def get_random_list(rng, low=2, high=8, tp="int"):
    if tp is "float":
        lst = [random.uniform(low, high) for i in range(rng)]
    elif tp is "int":
        lst = [randint(0, 99) for i in range(rng)]
    return lst


ln = 100000


# selection sort
def selection_sort(lst):
    for current_index in range(ln - 1):
        min_index = current_index  # current index is min index
        next_index = current_index + 1  # get nex index
        for j in range(next_index, ln):
            if lst[j] < lst[min_index]:  # if next element < current element
                min_index = j  # then write index with smaller element in m
        lst[current_index], lst[min_index] = lst[min_index], lst[current_index]


def bubble_sort(lst):
    for j in range(ln - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def insertion_sort(lst):
    for i in range(ln):
        j = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1


test_list = get_random_list(ln)
selection_sort_list = list(test_list)
insertion_sort_list = list(test_list)
bubble_sort_list = list(test_list)

before = datetime.datetime.now()
selection_sort(selection_sort_list)
after = (datetime.datetime.now() - before)
standart_sort_list = list(test_list)
standart_sort_list.sort()
print("selection sort time", after, "correctly sorted = ",
      True if standart_sort_list == selection_sort_list else False)

before = datetime.datetime.now()
insertion_sort(insertion_sort_list)
after = (datetime.datetime.now() - before)
print("insertion sort time", after, "correctly sorted = ",
      True if standart_sort_list == insertion_sort_list else False)

before = datetime.datetime.now()
bubble_sort(bubble_sort_list)
after = (datetime.datetime.now() - before)
print("bubble sort time", after, "correctly sorted = ",
      True if standart_sort_list == bubble_sort_list else False)
