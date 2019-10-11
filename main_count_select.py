import numpy as np
import timeit
import pandas as pd
import statistics
import matplotlib.pyplot as plt


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


def counting_range_select(ar, k, a, b, inclusive_a, inclusive_b):
    c = [0] * k
    for i in range(len(ar)):
        c[ar[i]] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    if b < a or a < 0 or b > len(c):
        print("fail")
    else:
        if inclusive_a and inclusive_b:
            if a == 0:
                print(c[b])
            else:
                print(c[b] - c[a - 1])
        elif inclusive_a:  # exclusive b
            if a == 0:
                print(c[b - 1])
            else:
                print(c[b - 1] - c[a])
        elif inclusive_b:  # exclusive a
            print(c[b] - c[a + 1])
        else:
            print(c[b - 1] - c[a + 1])


def create_random_array(number_of_elements):
    return np.random.randint(0, 9, number_of_elements)


def count_select(start, stop, by, file='count_select.txt'):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import counting_range_select
import numpy as np
ar = create_random_array(a_size)
k = np.amax(ar) + 1
c = [0] * k
a = 3
b = np.amax(ar) - 1
inclusive_a = True
inclusive_b = True'''
    TEST_CODE = '''
counting_range_select(ar, k, a, b, inclusive_a, inclusive_b)'''

    times = list()
    for i in range(start, stop, by):
        time = timeit.repeat(setup=SETUP_CODE.replace('a_size', str(i)),
                             stmt=TEST_CODE,
                             number=100,
                             repeat=10)
        a_time = statistics.mean(time)
        times.append(a_time)
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


if __name__ == '__main__':
    starts = 10
    stops = 1000
    bys = 10
    count_select_time = count_select(starts, stops, bys)
    data = pd.DataFrame({'x': range(starts, stops, bys), 'count': count_select_time})
    plt.plot('x', 'count', data=data)
    plt.legend()
    plt.show()

