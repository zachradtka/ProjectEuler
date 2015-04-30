def fibb(n0, n1):
    """
    A recursive fibonacci generator
    """
    n2 = n0 + n1
    yield n2
    for val in fibb(n1, n2):
        yield val

def sumEvens(limit):
    """
    A function to sum all of the evens in a fibonacci sequence
    """
    sum = 0
    for i in fibb(0,1):
        if i > limit :
            return sum
        elif i%2 == 0:
            sum +=i
    return sum

def main():
    print('Answer: %d' % sumEvens(4000000))

if __name__ == '__main__':
    main()