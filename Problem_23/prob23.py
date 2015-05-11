def proper_divisor(num):
    factors = set([1])

    prev_dividend = num

    for factor in xrange(2, num):

        if num%factor == 0:

            dividend = num/factor

            if prev_dividend <= factor:
                return factors

            # Add the number and divisor to the set of factors
            factors.add(factor)
            factors.add(dividend)
            prev_dividend = dividend

    return factors


def generate_abundant_sums(abundant_nums, new_num):
    abundant_sums = set()

    for i in abundant_nums:
        abundant_sums.add(i+new_num)

    return abundant_sums



def main():

    abundant_num = set()
    abundant_sums = set()

    non_summable = set()


    for i in range(1,28125):

        # Get the proper divisors of the current number
        proper_factors = proper_divisor(i)

        # Determine if is abundant
        if sum(proper_factors) > i:
            # print('%d is abundant' % i)
            abundant_num.add(i)
            abundant_sums = abundant_sums.union(generate_abundant_sums(abundant_num, i))


        if i not in abundant_sums:
            print('%d is non-summable' % i)
            non_summable.add(i)


    print(sum(non_summable))


if __name__ == '__main__':
    main()
