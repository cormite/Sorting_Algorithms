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
    def random_generator(items):
        """
        Generates an array initialized with randomized values

        :param items: Size of array to be initialized
        :return: Array initialized with random values from 1 to items
        """
        import random
        return [random.randint(1, items) for num_items in range(items)]

array_size = 10000

main = Main()
sort = sorting_algorithms.SortingAlgorithms()

random_items = main.random_generator(array_size)


function_list = [sort.bucket_sort,
                 sort.bubble_sort,
                 sort.counting_sort,
                 sort.cycle_sort,
                 sort.insertion_sort,
                 sort.merge_sort,
                 sort.shell_sort,
                 sort.quick_sort,
                 sort.radix_sort,
                 sort.heap_sort]

functions_names = ["Bucket Sort",
                   "Bubble Sort",
                   "Counting Sort",
                   "Cycle Sort",
                   "Insertion Sort",
                   "Merge Sort",
                   "Shell Sort",
                   "Quick Sort",
                   "Radix Sort",
                   "Heap Sort"]

for index, value in enumerate(function_list):
    # A new list has to be used otherwise after the first execution of the for
    # loop the list is already sorted.
    unsorted = random_items[:]
    if functions_names[index] != "Counting Sort":
        start_time = time.time()
        function_list[index](unsorted)
    else:
        start_time = time.time()
        function_list[index](unsorted, len(unsorted))
    print("--- seconds for " + functions_names[index].rjust(14)
          + " : "
          + "{0}".format(time.time() - start_time))


