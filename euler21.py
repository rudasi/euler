
def properDivisors(numbers):
   import math
   am_pairs = {} 
   am_list = []
   for val in numbers:
      divisors = []
      for i in range(1,int(math.sqrt(val))+1):
	 if (val%i == 0):
            divisors.append(i)
            divisors.append(val/i)
      am_pairs[val] = sum(divisors) - val
   
   for val in am_pairs.keys():
      key = am_pairs[val]
      if key in am_pairs.keys():
	 if (key != val):
            if (am_pairs[key] == val):
               am_list.append(val)
	       am_list.append(am_pairs[val])
   
   am_list = set(am_list)
   print am_list
   print sum(am_list)
   
if __name__ == "__main__":
   numbers = [i for i in range(1,10001)]
   properDivisors(numbers)
