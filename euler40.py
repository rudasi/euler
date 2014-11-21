num_str = ''
num = 0
for i in range (0,1000000):
   num = num + 1
   num_str += str(num)

val = int(num_str[0]) * int(num_str[99]) * int(num_str[999]) * int(num_str[9999]) * int(num_str[99999]) * int(num_str[999999])
print val
