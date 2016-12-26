#!/usr/bin/env python
# -*- coding: utf-8 -*-

# References:
# https://en.wikipedia.org/wiki/Sorting_algorithm


class SortingAlgorithms:


    # Extra Functions
    @staticmethod
    def hashing(items):
        import math
        m = items[0]
        for i in range(1, len(items)):
            if (m < items[i]):
                m = items[i]
        result = [m, int(math.sqrt(len(items)))]
        return result

    @staticmethod
    def re_hashing(i, code):
        return int(i / code[0] * (code[1] - 1))

    # Simple Sorts

    # [Best: O(n), Worst:O(N^2)]
    @staticmethod
    def bubble_sort(items):
        """ Implementation of bubble sort """
        for i, a in enumerate(items):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]  # Swap!

    def bucket_sort(self, items):
        """
        Implementation of Sorting Method Bucket Sort.

        :type       items: list
        :param      items: list to be ordered
        :rtype:     list
        :return:    items incrementally ordered
        """
        # get hash codes
        code = self.hashing(items)
        buckets = [list() for _ in range(code[1])]
        # distribute data into buckets: O(n)
        for i in items:
            x = self.re_hashing(i, code)
            buck = buckets[x]
            buck.append(i)

        for bucket in buckets:
            self.quick_sort(bucket)

        ndx = 0
        # merge the buckets: O(n)
        for i, b in enumerate(buckets):
            for v in b:
                items[ndx] = v
                ndx += 1

    # [Best: O(N), Worst:O(N^2)]
    @staticmethod
    def insertion_sort(items):
        """ Implementation of insertion sort """
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1

    # [Best/Worst: O(N^2)]
    @staticmethod
    def selection_sort(items):
        for fillslot in range(len(items) - 1, 0, -1):
            position_of_max = 0
            for location in range(1, fillslot + 1):
                if items[location] > items[position_of_max]:
                    position_of_max = location

            temp = items[fillslot]
            items[fillslot] = items[position_of_max]
            items[position_of_max] = temp

    # Efficient Sorts

    # [Best/Avg/Worst: O(N lg N)]
    @staticmethod
    def heap_sort(items):
        """ Implementation of heap sort """
        import heapq
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]

    def merge_sort(self, items):
        if len(items) > 1:
            mid = len(items) // 2
            lefthalf = items[:mid]
            righthalf = items[mid:]

            self.merge_sort(lefthalf)
            self.merge_sort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    items[k] = lefthalf[i]
                    i = i + 1
                else:
                    items[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                items[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                items[k] = righthalf[j]
                j = j + 1
                k = k + 1
        return items

    @staticmethod
    def shell_sort(items):
        "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
        gap = len(items) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(items)):
                val = items[i]
                j = i
                while j >= gap and items[j - gap] > val:
                    items[j] = items[j - gap]
                    j -= gap
                items[j] = val
            gap //= 2

    # [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
    def quick_sort(self, items):
        """ Implementation of quick sort """
        if len(items) > 1:
            pivot_index = len(items) // 2
            smaller_items = []
            larger_items = []

            for i, val in enumerate(items):
                if i != pivot_index:
                    if val < items[pivot_index]:
                        smaller_items.append(val)
                    else:
                        larger_items.append(val)

            self.quick_sort(smaller_items)
            self.quick_sort(larger_items)
            items[:] = smaller_items + [items[pivot_index]] + larger_items

    # [Best/Avg/Worst: O(N)]
    @staticmethod
    def radix_sort(items):
        RADIX = 10
        max_length = False
        tmp, placement = -1, 1

        while not max_length:
            max_length = True
            # declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # split aList between lists
            for i in items:
                tmp = i / placement
                buckets[tmp % RADIX].append(i)
                if max_length and tmp > 0:
                    max_length = False

            # empty lists into aList array
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    items[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX

