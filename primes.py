
def primes(n):
   """This function returns a tuple of 2 list. The first list is a boolean
   list where a True value at an index indicates a prime number. The second list
   is a list of the prime numbers. The parameter for this function is the number
   till which primes should be calculated"""

   import math

   prime = [True] * (n+1)
   prime[0] = False;
   prime[1] = False;

   root = int(math.sqrt(n))
   for i in range(2,root+1):
      if (prime[i]):
	 k = i*i
	 while k < (n + 1): 
            prime[k] = False;
	    k += i
   
   prime_numbers = []
   
   for i in range(len(prime)):
      if (prime[i] == True):
	 prime_numbers.append(i)

   return (prime, prime_numbers)

if __name__ == "__main__":
   (prime, prime_number) = primes(100)
   print prime_number
