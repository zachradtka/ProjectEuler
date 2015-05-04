import math
import sys

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        
        if num%2 == 0:
            return False
        
        for i in xrange(3,int(math.sqrt(num) + 1),2):
            if num%i == 0:
                return False

        return True

    return False


def generate_primes(limit):
    for i in xrange(1,limit):
        if is_prime(i):
            yield i



def main():
    sum = 0

    limit = int(sys.argv[1])

    for prime in generate_primes(limit):
        sum+=prime

    print('Sum of primes below %d is %d' % (limit, sum))

if __name__ == '__main__':
    main()