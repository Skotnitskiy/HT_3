from random import randint
import random


def get_random_list(rng, low=2, high=8, type="int"):
    if type is "float":
        lst = [random.uniform(low, high) for i in range(rng)]
    elif type is "int":
        lst = [randint(0, 8000) for i in range(rng)]
    return lst


# selection sort
def selection_sort(lst):
    list_len = len(lst)
    for current_index in range(list_len - 1):
        min_index = current_index  # current index is min index
        next_index = current_index + 1  # get nex index
        for j in range(next_index, list_len):
            if lst[j] < lst[min_index]:  # if next element < current element
                min_index = j  # then write index with smaller element in m
        lst[current_index], lst[min_index] = lst[min_index], lst[current_index]
    return lst


def bubble_sort(lst):
    ln_lst = len(lst)
    for j in range(ln_lst - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
