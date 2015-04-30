import math
import sys

def is_triplet(a,b,c):
    if a**2 + b**2 != c**2:
        return False
    if a>=b or a>=c or b>=c:
        return False
    return True


def generate_triplet(c=5):
    while True:
        # divisors = generate_divisors(c**2)

        # num_divisors = len(divisors)
        # Ensure there are more than 2 divisors
        # if num_divisors >= 2:
        for a in xrange(1,c):
            for b in xrange(2, c):
                if is_triplet(a,b,c):
                    yield (a,b,c)

        # Increment C
        c+=1

def find_sum(num):
    for (a,b,c) in generate_triplet():
        if a+b+c == num:
            return (a,b,c)

def main():
        num = int(sys.argv[1])
        (a,b,c) = find_sum(num)

        print('Triplet: %d %d %d' % (a, b, c))
        print('%d*%d*%d = %d' % (a, b, c, a*b*c))


if __name__ == '__main__':
    main()