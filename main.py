#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sorting_algorithms
import time


class Main:

    @staticmethod
    def random_generator():
        import random

        elems = 10000

        random_items = [random.randint(1, elems) for num_items in range(elems)]
        return random_items


main = Main()
sort = sorting_algorithms.SortingAlgorithms()

random_items = main.random_generator()
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

