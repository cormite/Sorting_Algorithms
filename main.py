#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sorting_algorithms
import time


class Main:

    def random_generator(self):
        import random

        elems = 1000000

        random_items = [random.randint(1, elems) for num_items in range(elems)]
        return random_items

main = Main()
sort = sorting_algorithms.Sorting_Algorithms()

random_items = main.random_generator()

items = main.random_generator()
start_time = time.time()
sort.bucket_sort(items)
print("--- seconds for Bucket Sort:    %s " % (time.time() - start_time))

# items = random_items[:]
# start_time = time.time()
# sort.bubble_sort(items)
# print("--- seconds for Bubble Sort:    %s " % (time.time() - start_time))

# items = random_items[:]
# start_time = time.time()
# sort.insertion_sort(items)
# print("--- seconds for Insertion Sort: %s " % (time.time() - start_time))

items = random_items[:]
start_time = time.time()
sort.merge_sort(items)
print("--- seconds for Merge Sort:     %s " % (time.time() - start_time))

items = random_items[:]
start_time = time.time()
sort.shell_sort(items)
print("--- seconds for Shell Sort:     %s " % (time.time() - start_time))

items = random_items[:]
start_time = time.time()
sort.quick_sort(items)
print("--- seconds for Quick Sort:     %s " % (time.time() - start_time))

items = main.random_generator()
start_time = time.time()
sort.radix_sort(items)
print("--- seconds for Radix Sort:     %s " % (time.time() - start_time))

items = random_items[:]
start_time = time.time()
sort.heap_sort(items)
print("--- seconds for Heap Sort:      %s " % (time.time() - start_time))

