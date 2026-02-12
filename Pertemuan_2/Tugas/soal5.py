import math

def jarak(x1, y1, x2, y2):
   d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
   return d

x1 = 2
y1 = 1
x2 = 3
y2 = 6

hasil = jarak(x1, y1, x2, y2)

print(f'jarak = {hasil:.2f}')