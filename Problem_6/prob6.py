def sum_of_squares(num):
    sum = 0
    for i in range(1, num+1):
        sum += i**2
    return sum

def square_of_sums(num):
    sum = 0
    for i in range(1, num+1):
        sum+=i

    return sum**2

def main():
    num = 100

    # difference
    print('square of sums minus sum of squares: %d' % (square_of_sums(num) - sum_of_squares(num) ))

if __name__ == '__main__':
    main()