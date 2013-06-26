
def tn(n):
   return ((n*(n+1))/2)

def pn(n):
   return ((n*(3*n-1))/2)

def hn(n):
   return (n*(2*n-1))

def check(n):
   val = []
   for i in xrange(1,n):
      if (tn(i) == pn(i) == hn(i)):
	 val.append(tn(i))

   print val 

def calc(n):
   answer = []
   t = []
   p = []
   h = []

   for i in range(1,n):
      t.append(tn(i))
      p.append(pn(i))
      h.append(hn(i))

   for val in t:
      if (val in p and val in t):
	 answer.append(val)
	 print t.index(val)
         if (len(answer) >= 4):
            print answer
            break

if __name__ == "__main__":
   #calc(30000)
   check(5000000000)

