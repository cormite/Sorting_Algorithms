#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import random
import sorting_algorithms


class Test (unittest.TestCase):

    sort = sorting_algorithms.Sorting_Algorithms()
    random_items = [random.randint(1, 1000) for num_items in range(1000)]

    def testBucketsort(self):
        items = self.random_items[:]
        self.sort.bucket_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("bucketsort method fails.")

    def testBubblesort(self):
        items = self.random_items[:]
        self.sort.bubble_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("bubblesort method fails.")

    def testHeapsort(self):
        items = self.random_items[:]
        self.sort.heap_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("heap method fails.")

    def testInsertionsort(self):
        items = self.random_items[:]
        self.sort.insertion_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("insertion method fails.")

    def testMergesort(self):
        items = self.random_items[:]
        self.sort.merge_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("merge method fails.")

    def testSelectionsort(self):
        items = self.random_items[:]
        self.sort.selection_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("selection method fails.")

    def testShellsort(self):
        items = self.random_items[:]
        self.sort.shell_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("shell method fails.")

    def testQuicksort(self):
        items = self.random_items[:]
        self.sort.quick_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("quick method fails.")

    def testRadix(self):
        items = self.random_items[:]
        self.sort.radix_sort(items)
        for i in range(1, len(items)):
            if items[i - 1] > items[i]:
                self.fail("radix method fails.")


if __name__ == '__main__':
    unittest.main()
