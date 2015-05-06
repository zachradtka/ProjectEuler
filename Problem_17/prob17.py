import sys


NUMBERS = {1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eight',
           9:'nine',
           10:'ten',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eighteen',
           19:'nineteen',
           20:'twenty',
           30:'thirty',
           40:'forty',
           50:'fifty',
           60:'sixty',
           70:'seventy',
           80:'eighty',
           90:'ninety',
           100:'hundred',
           1000:'thousand'}


def convert_number_to_text(number):
   text = ''

   # Determine thousand
   result = number / 1000
   if result > 0:
      
      text+=NUMBERS[result]
      text+=NUMBERS[1000]

      # Get the remainder
      number = number % 1000

   # Determine hundred
   result = number / 100
   if result > 0:
      text+=NUMBERS[result]
      text+=NUMBERS[100]

      # Get the remainder
      number = number % 100

   # Determine 10
   result = number / 10
   if result > 0:

      # Add 'and'
      if len(text) > 0:
         text+='and'

      if result > 1:
         text+=NUMBERS[result*10]

         # Get the remainder
         number = number % 10

         if number > 0:
            text+=NUMBERS[number]

      else:
         text+=NUMBERS[number]
         number = 0

   elif number > 0:

      # Add 'and'
      if len(text) > 0:
         text+='and'

      text+=NUMBERS[number]

   return text

def main():
   number = int(sys.argv[1])

   sum = 0

   for num in range(1, number):
      currNum = convert_number_to_text(num)
      print('%d: %s' % (num, currNum))
      sum+=len(currNum)

   print('Sum of characters for %d is %d' % (number, sum))


if __name__ == '__main__':
   main()