
def divisors(n):
   total = 0
   while (not n%2):
      total *= n/2
      n = n/2
