from primes import primes

def prime_sum(primes):
   length = 0
   for prime in primes:
      for i in range(0, primes.index(prime)):
         val = 0
	 for j in range(i,primes.index(prime)):
	    val += primes[j]
            if (val == prime):
	       if ((j - i + 1) > length):
		  print val
	          length = j - i + 1
            if (val > prime):
	       break

   return length
if __name__ == "__main__":
   prime, prime_number = primes(1000000)
   print prime_sum(prime_number)
   

