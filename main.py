import random
import numpy as np
import timeit
import pandas as pd
import matplotlib.pyplot as plt
import statistics


def partition(ar, p, r):
    i = (p - 1)
    pivot = ar[r]
    for j in range(p, r):
        if ar[j] <= pivot:
            i = i + 1
            ar[i], ar[j] = ar[j], ar[i]
    ar[(i + 1)], ar[r] = ar[r], ar[(i + 1)]
    return i + 1


def random_partition(ar, p, r):
    i = random.randint(p, r)
    ar[r], ar[i] = ar[i], ar[r]
    return partition(ar, p, r)


def random_select(ar, p, r, i):
    if p == r:
        return ar[p]
    q = random_partition(ar, p, r)
    k = q - p + 1
    if i == k:
        return ar[q]
    elif i < k:
        return random_select(ar, p, q-1, i)
    else:
        return random_select(ar, q+1, r, i-k)


def iterative_random_select(ar, i):
    p = 0
    r = len(ar) - 1
    while True:
        if p == r:
            return ar[p]
        q = random_partition(ar, p, r)
        k = q - p + 1
        if i == k:
            return ar[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i = i-k


def counting_sort(a, b, k):
    c = [0] * k
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(len(c)):
        c[i] -= 1
    for i in range(len(a), 0, -1):
        b[c[a[i - 1]]] = a[i - 1]
        c[a[i - 1]] -= 1
    return b


def quick_sort(ar, p, r):
    if p < r:
        q = random_partition(ar, p, r)
        quick_sort(ar, p, q-1)
        quick_sort(ar, q+1, r)


def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        k = i - 1
        while k >= 0 and key < ar[k]:
            ar[k + 1] = ar[k]
            k -= 1
        ar[k + 1] = key
    return ar


def create_random_array(number_of_elements):
    return np.random.randint(0, 100000, number_of_elements)


def counting_sort_select_time(start, stop, by, file):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import counting_sort
import numpy as np
a = create_random_array(a_size)
i = 4
k = np.amax(a) + 1
b = [0] * len(a)'''
    TEST_CODE = '''
a = counting_sort(a, b, k)
a[i]'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        times.append(statistics.mean(time))
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


def quick_sort_select_time(start, stop, by, file):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import quick_sort
from __main__ import random_partition
from __main__ import partition
import numpy as np
a = create_random_array(a_size)
i = 4
p = 0
r = len(a) - 1'''
    TEST_CODE = '''
quick_sort(a, p, r)
a[i]'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        times.append(statistics.mean(time))
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


def insertion_sort_select_time(start, stop, by, file):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import insertion_sort
import numpy as np
a = create_random_array(a_size)
i = 4'''
    TEST_CODE = '''
insertion_sort(a)
a[i]'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        times.append(statistics.mean(time))
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


def iterative_random_select_time(start, stop, by, file):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import iterative_random_select
from __main__ import random_partition
from __main__ import partition
import numpy as np
ar = create_random_array(a_size)
i = 4'''
    TEST_CODE = '''
iterative_random_select(ar, i)'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        times.append(statistics.mean(time))
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


def random_select_time(start, stop, by, file):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import random_select
from __main__ import random_partition
from __main__ import partition
import numpy as np
ar = create_random_array(a_size)
i = 4
p = 0
r = len(ar) - 1'''
    TEST_CODE = '''
random_select(ar, p, r, i)'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        times.append(statistics.mean(time))
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


if __name__ == '__main__':
    starts = 100
    stops = 50000
    bys = 100
    print("Start")
    #sort_select_insertion_times = insertion_sort_select_time(starts, stops, bys, 'sort_select_insertion.txt')
    #print("complete insertion")
    #sort_select_quick_times = quick_sort_select_time(starts, stops, bys, 'sort_select_quick.txt')
    #print("complete quick")
    #sort_select_counting_times = counting_sort_select_time(starts, stops, bys, 'sort_select_counting.txt')
    #print("complete counting")
    iterative_random_select_times = iterative_random_select_time(starts, stops, bys, 'iterative_random_select.txt')
    print("complete iterative random")
    random_select_times = random_select_time(starts, stops, bys, 'random_select.txt')
    print("complete random")

    data = pd.DataFrame({'x': range(starts, stops, bys),
                         #'insertion_sort_select': sort_select_insertion_times,
                         #'quick_sort_select': sort_select_quick_times,
                         #'counting_sort_select': sort_select_counting_times,
                         'iterative_random_select': iterative_random_select_times,
                         'random_select': random_select_times})
    #plt.plot('x', 'insertion_sort_select', data=data)
    #plt.plot('x', 'quick_sort_select', data=data)
    #plt.plot('x', 'counting_sort_select', data=data)
    plt.plot('x', 'iterative_random_select', data=data)
    plt.plot('x', 'random_select', data=data)
    plt.legend()
    plt.show()



