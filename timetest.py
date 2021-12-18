import time
import random
from tz3_main import min_in_file, max_in_file, proizv_of_file, sum_of_file, square_root_of_sum


def time_of_operations():
    durations = []
    numbers_of_values = [2000, 5000, 8000, 11000]
    test_file = []
    for i in range(len(numbers_of_values)):
        for j in range(numbers_of_values[i]):
            test_file.append(int(random.randint(-10000, 10000)))
        start_time = time.time()
        exec('min_in_file(test_file)')
        exec('max_in_file(test_file)')
        exec('proizv_of_file(test_file)')
        exec('sum_of_file(test_file)')
        exec('square_root_of_sum')
        durations.append(time.time() - start_time)
        print('время выполнения файла с ', numbers_of_values[i], 'числами равна ',durations[i], 'сек')
        test_file.clear()


time_of_operations()