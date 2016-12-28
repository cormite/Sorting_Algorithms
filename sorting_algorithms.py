#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SortingAlgorithms:
    """ Implementation of Sorting Algorithms

    This class provides different sorting algorithms. The purpose of this
    project is to learn and measure the efficiency of each one of the
    algorithms when sorting an array of x items randomly initialized.

    **References**:
    *https://en.wikipedia.org/wiki/Sorting_algorithm*

    """

    # Simple Sorts

    # [Best: O(n), Worst:O(N^2)]
    @staticmethod
    def bubble_sort(items):
        """ Implementation of Bubble Sort """
        for i, a in enumerate(items):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]  # Swap!

    def bucket_sort(self, items):
        """
        Implementation of Bucket Sort.
        Reference: http://www.geekviewpoint.com/python/sorting/bucketsort

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
        #for i, b in enumerate(buckets):
        for _, b in enumerate(buckets):
            for v in b:
                items[ndx] = v
                ndx += 1

    @staticmethod
    def counting_sort(aList, k):
        counter = [0] * (k + 1)
        for i in aList:
            counter[i] += 1

        ndx = 0;
        for i in range(len(counter)):
            while 0 < counter[i]:
                aList[ndx] = i
                ndx += 1
                counter[i] -= 1

    def cycle_sort(self, aList):
        writes = 0

        for cs in range(len(aList) - 1):
            # assume the element at aList[cs] is out of place
            seeker = aList[cs]
            pos = cs
            # find the correct position (pos) of seeker
            for i in range(cs + 1, len(aList)):
                if aList[i] < seeker:
                    pos += 1

            # if seeker is already in correct position, move on
            if pos == cs:
                continue

            # move index pos after duplicates if any
            while seeker == aList[pos]:
                pos += 1

            # Make a switch: seeker gets index pos, its rightful
            # home; whatever element was at pos is now the seeker
            # in search of a rightful home.

            seeker = self.set_value(aList, seeker, pos)
            # track the number of writes
            writes += 1

            #  complete the current cycle before moving to the next
            #  cycle. At the end of the current cycle, pos will
            #  equal cs; which should make sense since a cycle
            #  always ends where it began.

            while pos != cs:
                # same as block of code above
                pos = cs
                for i in range(cs + 1, len(aList)):
                    if aList[i] < seeker:
                        pos += 1

                while seeker == aList[pos]:
                    pos += 1

                seeker = self.set_value(aList, seeker, pos)
                writes += 1

        return writes

    @staticmethod
    def insertion_sort(items):
        # [Best: O(N), Worst:O(N^2)]
        """ Implementation of Insertion Sort """
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1

    @staticmethod
    def selection_sort(items):
        # [Best/Worst: O(N^2)]
        """ Implementations of Selection Sort """
        for fillslot in range(len(items) - 1, 0, -1):
            position_of_max = 0
            for location in range(1, fillslot + 1):
                if items[location] > items[position_of_max]:
                    position_of_max = location

            temp = items[fillslot]
            items[fillslot] = items[position_of_max]
            items[position_of_max] = temp

    # Efficient Sorts

    @staticmethod
    def heap_sort(items):
        # [Best/Avg/Worst: O(N lg N)]
        """ Implementation of Heap Sort """
        import heapq
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]

    def merge_sort(self, items):
        """ Implementation of Merge Sort """
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
        """ Implementation of Shell Sort
        using Shell's (original) gap sequence: n/2, n/4, ..., 1. """
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

    def quick_sort(self, items):
        # [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
        """ Implementation of Quick Sort """
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

    @staticmethod
    def radix_sort(items):
        # [Best/Avg/Worst: O(N)]
        """ Implementation of Radix Sort """
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

    @staticmethod
    def set_value(aList, data, ndx):
        try:
            return aList[ndx]
        finally:
            aList[ndx] = data

    # Extra Functions
    @staticmethod
    def hashing(items):
        """ Implementation of hashing used by Bucket Sort """
        import math
        m = items[0]
        for i in range(1, len(items)):
            if m < items[i]:
                m = items[i]
        result = [m, int(math.sqrt(len(items)))]
        return result

    @staticmethod
    def re_hashing(i, code):
        """ Implementation of re_hashing used by Bucket Sort """
        return int(i / code[0] * (code[1] - 1))

