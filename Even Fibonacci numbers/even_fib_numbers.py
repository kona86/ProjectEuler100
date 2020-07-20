
'''
# TODO:
- Use a generator expression/function later
instead of a typical function
'''
from functools import reduce
from itertools import accumulate
# num is the nth term

# fibbonnaci list


def fib(nterms):
    n1, n2 = 0, 1
    nth = 0
    count = 0
    numbers = []
# check if the number of terms is valid
    if nterms <= 0:
        numbers.append(n2)
        return numbers
    elif nterms == 1:
        numbers.append(1)
        return numbers
    else:
        while count < nterms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth  # last nterm
            count += 1
            numbers.append(n2)
    return numbers


def main():
    def expr(x,y):
    if (x and y % 2 == 0):
        return x
    arr = fib(10)  # e6 equavlent to 6 zero
    x = map(expr(x,y), arr)  # is even
    return x


if __name__ == "__main__":
    main()
