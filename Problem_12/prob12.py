import sys

def triangle_seq():
    sum = 0
    num = 1
    while True:
        sum+=num
        yield sum
        num+=1

def get_factors(num):
    factors = [1,num]

    prev_dividend = num

    for factor in xrange(2, num):

        if num%factor == 0:

            dividend = num/factor

            if prev_dividend <= factor:
                return factors

            # Add the number and divisor to the list of factors
            factors.extend([factor, dividend])
            prev_dividend = dividend

    return factors

def main():

    num_divisors = int(sys.argv[1])

    for i in triangle_seq():
        
        factors = get_factors(i)
        if len(factors) > num_divisors:
            print('Number of factors: %d' % (i))
            break

if __name__ == '__main__':
    main()