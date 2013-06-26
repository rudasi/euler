from primes import primes

prime = None
prime_numbers = None
N = 0
A = 0
B = 0

def is_prime(val):
   global prime
   if (val < 0):
      return False

   if (prime[val]):
      return True
   return False

def equation(a,b):
   global A
   global B
   global N

   for n in range(0,1000):
      if (is_prime(n*n + (a*n) + b)):
	 continue
      else:
	 if (n > N):
            N = n
	    A = a
	    B = b
	 break
	      
if __name__ == "__main__":
   (prime, prime_numbers) = primes(1000000)

   for a in xrange(-1000,1001):
      for b in xrange(-1000,1001):
	 equation(a,b)
   print str(N) + "  " + str(A) + "  " + str(B)

