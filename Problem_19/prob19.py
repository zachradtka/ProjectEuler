DAYS = 365


def days_in_month(year, month):
   
   if month == 2:
      if is_leap_year(year):
         return 29

      return 28

   elif month in [4, 6, 9, 11]:
      return 30

   return 31

def days_in_year(year):
   if (is_leap_year(year)):
      return DAYS + 1

   return DAYS

def is_leap_year(year):
   if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
      return True

   return False


def is_sunday(day):
   if day % 7 ==0:
      return True

   return False

def num_sundays(start, end):
   days = 0

   for year in range(start, end+1):
      days += days_in_year(year)

   
   return days/7


def main():
   
   start = 1901
   end = 2001

   day = 1 + days_in_year(1900)
   first_sundays = 0


   # Loop through first year
   for year in range(start, end):

      for month in range(1,13):

         # If the day is a Sunday, increase the number of Sundays 
         # that occur on the first of the month
         if is_sunday(day):
            first_sundays+=1

         day+=days_in_month(year, month)

   print('Number of Sundays that fell on the first of the month= %d' % (first_sundays))


if __name__ == '__main__':
   main()