#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sorting_algorithms
import time


class Main:

    def random_generator(self):
        import random

        elems = 10000

        random_items = [random.randint(1, elems) for num_items in range(elems)]
        return random_items


main = Main()
sort = sorting_algorithms.Sorting_Algorithms()

random_items = main.random_generator()
function_list = [sort.bucket_sort, sort.bubble_sort, sort.insertion_sort, sort.merge_sort, sort.shell_sort, sort.quick_sort, sort.radix_sort, sort.heap_sort]
functions_names = ["Bucket Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Shell Sort", "Quick Sort", "Radix Sort", "Heap Sort"]

for functions in range(0, len(function_list)):
    start_time = time.time()
    function_list[functions](random_items[:])
    print("--- seconds for "+functions_names[functions]+" :    %s " % (time.time() - start_time))
