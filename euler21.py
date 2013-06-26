
def properDivisors(numbers):
   import math
   am_pairs = []
   for val in numbers:
      divisors = []
      for i in range(1,int(math.sqrt(val))+1):
	 if (val%i == 0):
            divisors.append(i)
            divisors.append(val/i)
      if ((sum(divisors) - val) == val):
	 am_pairs.append(val)
   
   print am_pairs
if __name__ == "__main__":
   numbers = [i for i in range(1,300)]
   properDivisors(numbers)
