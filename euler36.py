
def is_palindrome(n):
   temp = n
   n = n[::-1]
   if (temp == n):
      return True
   return False

def to_binary(n):
   val = bin(n)
   val = str(val)
   val = val[2:]
   return val

def total_sum(n):
   total = 0
   for i in range(0,n+1):
      temp = to_binary(i)
      if (is_palindrome(temp) and is_palindrome(str(i))):
         total += int(i)
   
   return total

if __name__ == "__main__":
   print total_sum(1000000)

