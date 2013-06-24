
def diag_sum(n):
   answer = 1
   temp = 1
   cur = 0
   for i in range(1,n/2 + 1):
      for j in range(1,5):
         cur = temp + (2*i*j)
       	 answer += cur 
      temp = cur

   return answer

if __name__ == "__main__":
   print diag_sum(1001)
     
	
