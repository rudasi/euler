months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
months_leap = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
years = {}

def is_leapyear(year):
   if (year%100 == 0):
      if (year%400 == 0 and year%4 == 0):
         return True
   elif (year%4 == 0):
      return True
   
   return False

for i in range (1901,2001):
   if (is_leapyear(i)):
      years[i] = 366
   else:
      years[i] = 365
      

if __name__ == "__main__":
   number_of_days = 0
   bitmap = []
   answer = 0
   flag = 0
   leap_count = 0

   for i in years.keys():
      number_of_days += years[i]
      
   bitmap = [0] * number_of_days

   for i in range(1901,2001):
      if (is_leapyear(i)):
	 flag = 1
	 leap_count += 1

      else:
	 flag = 0
      for j in range(1,13):
         if (flag):
            position = ((i - 1901)) * 365 + leap_count
      

   for i in years.keys():
      if (years[i] == 365):
         
   
