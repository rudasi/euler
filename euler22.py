val = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

def score(name):
   total = 0
   for letter in name:
      total += val[letter]
   return total

def total_score(names):
   total = 0
   for name in names: 
      total += score(name) * (names.index(name) + 1)
   
   return total

if __name__ == "__main__":
   f = open("names.txt","r")
   names = f.read()
   f.close()
   names = names.split(",")
   names = [name.strip("\"") for name in names]
   names.sort()

   print total_score(names)
