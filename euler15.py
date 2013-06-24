factorial_hash = {}

def factorial(n):
   
   if (n in factorial_hash.keys()):
      return factorial_hash[n]
   
   elif (n == 0 or n == 1):
      factorial_hash[n] = 1
      return 1

   else:
      val = factorial(n-1) * n
      factorial_hash[n] = val
      return val

def combinations(a,b):
   return (factorial_hash[a]/(factorial_hash[b] * factorial_hash[a-b]))



if __name__ == "__main__":
   
   coefficients = []
   answer = 0

   for i in range(0,21):
      factorial(i)

   for i in range(0,21):
      coefficients.append(combinations(20,i))

   for i in coefficients:
      answer += i*i

   print answer
      
   
