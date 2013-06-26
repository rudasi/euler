
score = {"\"":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

def tn(n):
   t = []
   for i in range(1,n+1):
      t.append((i*(i+1))/2)

   return t

def calc_score(words, t):
   count = 0
   for word in words:
      temp = 0
      for letter in word:
         temp += score[letter]

      if (temp in t):
         count += 1

   print count

if __name__ == "__main__":
   f = open("words.txt","r")
   data = f.readlines()
   f.close()

   words = data[0].split(",")
   t = tn(1000)
   calc_score(words,t)
