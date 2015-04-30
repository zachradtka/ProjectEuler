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

def generate_nth_prime(n):
    nth_prime = 0
    curr_num = 1
    while nth_prime < n:
        curr_num+=1
        if is_prime(curr_num):
            nth_prime+=1
    return curr_num

def main():
    nth_prime = int(sys.argv[1])


    print('The %d prime is: %d' % (nth_prime, generate_nth_prime(nth_prime)))

if __name__ == '__main__':
    main()