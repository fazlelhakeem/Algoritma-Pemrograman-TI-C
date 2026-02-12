import math

def bilangan_prima(n):
   prima = []

   if n <= 1:   
      return 'Tidak ada'

   for i in range(2, n+1):
      enter = True
      for x in range(2, int(math.sqrt(i)) +1):
         if i % x == 0:
            enter = False
   
      if enter == True:
         prima.append(i)

   return prima

n = 50
print(bilangan_prima(n))