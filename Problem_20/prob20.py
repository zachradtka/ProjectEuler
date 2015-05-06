import math

def main():
   num = math.factorial(100)

   numbers = list(str(num))

   sum = 0
   for i in numbers:
      sum+=int(i)

   print('Sum is: %d' % (sum))

if __name__ == '__main__':
   main()