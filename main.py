#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sorting_algorithms
import time


class Main:
    """ Simple Class which:
        1) Defines the number of elements to be sorted in ELEMS
        2) Generates the array with random values
        3) Calls the Sorting Algorithms and measures how long it took to sort.
    """

    @staticmethod
    def random_generator(ELEMS):
        '''Generates an array initialized with randomized values'''
        import random
        return [random.randint(1, ELEMS) for num_items in range(ELEMS)]

ELEMS = 10000

main = Main()
sort = sorting_algorithms.SortingAlgorithms()

random_items = main.random_generator(ELEMS)

function_list = [sort.bucket_sort, sort.bubble_sort, sort.insertion_sort,
                 sort.merge_sort, sort.shell_sort, sort.quick_sort,
                 sort.radix_sort, sort.heap_sort]
functions_names = ["Bucket Sort", "Bubble Sort", "Insertion Sort",
                   "Merge Sort", "Shell Sort", "Quick Sort",
                   "Radix Sort", "Heap Sort"]

for index, value in enumerate(function_list):
    start_time = time.time()
    function_list[index](random_items)
    print("--- seconds for " + functions_names[index] +
          " :    {0} ".format(time.time() - start_time))

