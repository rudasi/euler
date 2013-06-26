def distinct_powers(a,b):
   values = []
   for i in range(2,a+1):
      for j in range(2,b+1):
	 if (pow(i,j) not in values):
	    values.append(pow(i,j))
   print len(values)

if __name__ == "__main__":
   distinct_powers(100,100)
