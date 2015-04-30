import math

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

def prime_factors(num):
    for prime in generate_primes(num):
        if num%prime == 0:
            print('%d is a prime factor' % prime)

def main():
    # for i in generate_primes(50):
    #     print i
    prime_factors(600851475143)

if __name__ == '__main__':
    main()
