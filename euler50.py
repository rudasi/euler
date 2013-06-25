from primes import primes

prime_dict = {}

def prime_sum(primes):
   length = 0
   for prime in primes:
      for i in range(0, primes.index(prime)):
         val = 0
	 for j in range(i,primes.index(prime)):
	    #if ((str(i)+","+str(j)) in prime_dict.keys()):
	       #val = prime_dict[str(i)+","+str(j)]
	    #else:
	       #val += primes[j]
	       #prime_dict[str(i)+","+str(j)] = val

            val 
            if (val == prime):
	       if ((j - i + 1) > length):
		  print val
	          length = j - i + 1
            if (val > prime):
	       break

   return length
if __name__ == "__main__":
   prime, prime_number = primes(10)
   cumulative_sum = []
   temp = prime_number[0]
   cumulative_sum.append(temp)

   for val in prime_number[1:]:
      cumulative_sum.append(val + temp)
      temp = val + temp

   print prime_sum(prime_number, cumulative_sum)
   

