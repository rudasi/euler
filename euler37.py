from primes import primes
   
trunc_primes = []

def truncatable_primes(prime, prime_numbers):
   global trunc_primes 
   for val in prime_numbers[4:]:
      flag = 1
      print "start"
      print val
      for i in range(len(str(val))):
	 print "---"
	 print str(val)[i:]
	 print str(val)[:-i] 

	 if (prime[int(str(val)[i:])] == True and prime[int(str(val)[-i:])] == True):
            a = 1 
         else:
            flag = 0

      if (flag == 1):
	 trunc_primes.append(val)
         if (len(trunc_primes) == 11): 
            return trunc_primes
   return trunc_primes
    

if __name__ == "__main__":
   (prime,prime_numbers) = primes(1000000)
   temp = truncatable_primes(prime,prime_numbers)
   answer = 0
   print temp
   for i in temp:
      answer += i
   print answer
