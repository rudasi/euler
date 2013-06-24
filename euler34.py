
factorial = {"0":1,"1":1,"2":2,"3":6,"4":24,"5":120,"6":720,"7":5040,"8":40320,"9":362880}

def factorial_digit():
   total = 0
   for val in range(10,10000000):
      val = str(val)
      temp = 0
      for digit in val:
         temp += factorial[digit]
      if (str(temp) == val):
         print temp
         total += int(temp)
   return total 

if __name__ == "__main__":
   answer = factorial_digit()
   print answer
