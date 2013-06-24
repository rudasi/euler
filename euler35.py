import math
from itertools import permutations

def list_of_primes(num):
   prime = [True for i in range(0,num+1)]
   prime[0] = False
   prime[1] = False
   m = int(math.sqrt(num))

   for i in range(2,m+1):
      if (prime[i]):
	 k = i * i
	 while (k <= num):
            prime[k] = False
	    k = k + i 

   return prime

def circular_primes(primes, bool_primes):
   circular_primes = []
   for p in primes:
      temp_primes = []
      flag = True 
      val = str(p)
      end = len(val)
      for i in range(0,end):
	val = str(val)
        if (len(val) == 1):
           circular_primes.append(p)
	   break
	
	val = val[1:] + val[0]
        val = int(val)
	if bool_primes[val]:
           temp_primes.append(val)
	   #bool_primes[val] = False
	   flag = False 
	else:
	   temp_primes = []
           flag = True
        
	if flag:
           break

      if (flag == False):
	 if len(temp_primes):
	    for temp in temp_primes:
	       if (temp in primes):
	          primes.remove(temp)
	          bool_primes[temp] = False
        
	 circular_primes.extend(temp_primes)
	 temp_primes = []
	 
   circular_primes = set(circular_primes)
   circular_primes = list(circular_primes)
   return circular_primes

if __name__ == "__main__":
   bool_primes = list_of_primes(1000000)
   int_primes = [i for i,val in enumerate(bool_primes) if val == True]
   c_primes = circular_primes(int_primes,bool_primes)
   c_primes.sort()
   print c_primes
   print ("\nThe lenght of primes is \n %d" %(len(c_primes)))
