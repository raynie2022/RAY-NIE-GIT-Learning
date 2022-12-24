import platform
import time

memo = [-1] * 1000
call_count = 0
1
#增加几行注释 试试commit and push!
def Fibonacci(index):
    global call_count
    call_count += 1
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return Fibonacci(index - 1) + Fibonacci(index - 2)


def better_fibonacci(index):
    temp, a, b = 0, 1, 1                    # 1
    if index < 1:                           # 1
        return 0                            # 1
    if index < 3:                           # 1
        return 1                            # 1
    for i in range(3, index + 1):           # n-1次
        temp = b                            # n-2次
        b = a + b                           # n-2次
        a = temp                            # n-2次
    return b


def Fibonacci_calculate(index):
    magic_number = 2.2360679774997896964091736687313
    A = (1 + magic_number) / 2
    B = (1 - magic_number) / 2
    return int((A ** index - B ** index) / magic_number)


def test(index):
    global call_count
    for i in range(0, index):
        call_count = 0
        start = time.process_time()
        result = Fibonacci(i)
        end = time.process_time()
        print("Fibonacci({}) = {} (call count: {}, time: {})".format(i, result, call_count, end - start))
        call_count = 0
        start = time.process_time()
        result = Better_Fib(i)
        end = time.process_time()
        print("Better_Fib({}) = {} (call count: {}, time: {})".format(i, result, call_count, end - start))
        call_count = 0
        start = time.process_time()
        Fibonacci_calculate(i)
        end = time.process_time()
        print("Fibonacci_calculate({}) = {} (call count: {}, time: {})".format(i, result, call_count, end - start))

def compare(index):
    global call_count
    for i in range(0, index):
        if Fibonacci(i) != Fibonacci_calculate(i):
            print("Fibonacci({}) != Fibonacci_calculate({})".format(i, i))
            return False
        else:
            print("Fibonacci({}) == Fibonacci_calculate({})".format(i, i))
    return True

def compare2(index):
    global call_count
    for i in range(0, index):
        if Better_Fib(i) != Fibonacci_calculate(i):
            print("Better_Fib({}) != Fibonacci_calculate({})".format(i, i))
            return False
        else:
            print("Better_Fib({}) == Fibonacci_calculate({})".format(i, i))
    return True

def compare_better_fibonacci_with_fibonacci(index):
    for i in range(1, index):
        if Fibonacci(i) != better_fibonacci(i):
            print("better_fibonacci({}) != Fibonacci({}), result: {}".format(i, i, False))
            print("compare_better_fibonacci_with_fibonacci({}) = {}".format(i, False))
            return False
        else:
            print("better_fibonacci({}) == Fibonacci({}), result: {}".format(i, i, True))
    print("compare_better_fibonacci_with_fibonacci({}) = {}".format(index, True))
    return True


def test1(index):
    print("Fibonacci test from 0 to {}, result: {}".format(index, compare(index)))

def test2(index):
    print("Fibonacci test from 0 to {}, result: {}".format(index, compare2(index)))





def check_relation_between_value_and_call_count(index):
    global call_count
    for i in range(0, index):
        call_count = 0
        fn = Fibonacci(i)
        fnplus1 = Fibonacci_calculate(i + 1)
        print(
            "Fibonacci({0:>3}) = {1:>12}, call count: {2:>12}, F({3:>3} + 1) = {4:>12}, count == 2 * F({5:>3} + 1) - 1 (YES/NO): {6}".format(
                i, fn, call_count, i, fnplus1, i, call_count == 2 * fnplus1 - 1))


if __name__ == '__main__':
    # wait for user input
    index = int(input("Enter the index of the Fibonacci number: "))
    #check_relation_between_value_and_call_count(index)
    #test(index)
    #test1(index)
    test2(index)

