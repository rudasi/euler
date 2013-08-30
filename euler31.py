coinlist = [1,2,5,10,20,50,100,200]
change = 200
val = 0
count = 0

def my_combinations(coinlist, change):
   global val
   global count

   if (val == change):
      count += 1
      val = 0
      return 1
      
   for c in [cur for cur in coinlist if cur <= (change - val)]:
      #if (c == change):
      #   count += 1
      #	 val = 0
      #   return 
      val = c + my_combinations(coinlist, change)

if __name__ == "__main__":
   my_combinations(coinlist, change)
   print count
