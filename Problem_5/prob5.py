def possible_numbers(num):
    """
    generator fucnction to step through the numbers by scaling by num * (num-1)
    """
    scale = num * (num-1)
    num = scale

    while True:
        yield num
        num+=scale

def is_divisible(num, limit):
    for i in range(2, limit+1):
        if num%i != 0:
            return False

    return True

def smallest_number(num):
    for i in possible_numbers(num):
        if is_divisible(i, num):
            return i

def main():
    print('%d is the smallest number' % smallest_number(20))

if __name__ == '__main__':
    main()