def proper_divisor(num):
    factors = [1]

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

   pair = []

   for i in range(1, 10000):

      if i not in pair:
         possible_pair = sum(proper_divisor(i))


         if i != possible_pair and i == sum(proper_divisor(possible_pair)):
            amicable_pair=[i, possible_pair]
            pair.extend(amicable_pair)
            

   print('Sum of Amicable Pairs: %d' % sum(pair))

if __name__ == '__main__':
   main()
