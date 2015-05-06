def main():
   power = 2 ** 1000
   numbers = list(str(power))

   sum = 0

   for i in numbers:
      sum+=int(i)

   print('Sum is %d' % (sum))


if __name__ == '__main__':
   main()