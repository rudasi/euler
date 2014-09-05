import itertools

number_dictionary = {0:False,1:False,2:False,3:False,4:False,5:False,
                     6:False,7:False,8:False,9:False}
fib_num = [2,3,5,7,11,13,17]
is_good = True
sum = 0

def substring_divisibility(num):
   global sum
   is_num = True
   val = str(num)
   start = 1
   end = 8
   if (len(val) == 9):
      start = 0
      end = 7

   for i in range(start,end):
      temp = int(val[i] + val[i+1] + val[i+2])
      if ((temp % fib_num[i-1]) != 0):
         is_num = False
         break
   if (is_num == True):
      print num
      sum = sum + num

def reset_dict():
   for key in number_dictionary.keys():
      number_dictionary[key] = False

def pandigital_numbers():
   global is_good
   reset_dict()
   numbers = '0123456789'
   l = itertools.permutations(numbers)
   perms = [int(''.join(x)) for x in l]
   for num in perms:
      val = str(num)
      for digit in val:
         if (number_dictionary[int(digit)] == False):
            number_dictionary[int(digit)] = True
         else:
            reset_dict()
            is_good = False
            break
      if (is_good == True):
         substring_divisibility(num)
      is_good = True

if __name__ == "__main__":
   #substring_divisibility(1406357289)
   pandigital_numbers()
   print sum
