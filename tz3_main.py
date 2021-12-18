from math import sqrt

def read_file():
    f = open("test file.txt", "r")
    file = []
    for i in f:
        file += i.split()
    for i in file:
        file = [float(item) for item in file]
    return file


def min_in_file(list):
    min_num = list[0]
    for i in range(len(list)):
        if min_num > list[i]:
            min_num = list[i]
    return min_num


def max_in_file(list):
    max_num = list[0]
    for i in range(len(list)):
        if max_num < list[i]:
            max_num = list[i]
    return max_num


def sum_of_file(list):
    summ = 0
    for i in list:
        summ += i
    return summ


def proizv_of_file(list):
    if len(list) != 0:
        current = 1
        for i in range(len(list)):
            try:
                current *= list[i]
            except ArithmeticError:
                print('ошибка переполнения')
                sys.exit(1)
        return current
    else:
        print(0)

def square_root_of_sum(list):
    summ = 0
    for i in list:
        summ += i
    root = sqrt(summ)

    return root

if __name__ == '__main__':
    print('произведение равно', proizv_of_file(read_file()))
    print('минимальное число:', min_in_file(read_file()))
    print('максимальное число:', max_in_file(read_file()))
    print('сумма чисел равна', sum_of_file(read_file()))
    print('квардратный корень суммы равен', square_root_of_sum(read_file()))


