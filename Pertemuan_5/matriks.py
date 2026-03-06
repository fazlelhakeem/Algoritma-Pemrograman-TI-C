A = [[5, 3, 1], 
     [2, 8, 4], 
     [6, 0, 7]] 

B = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]] 

def tambah(A, B):
   baris, kolom = len(A), len(A[0])
   hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]

   return hasil

C_tambah = tambah(A, B)

def kurang(A, B):
   baris, kolom = len(A), len(A[0])
   hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]

   return hasil

C_kurang = kurang(A, B)

def skalar(A, k):
   hasil = []

   for i in A:
      x = [j * k for j in i]
      hasil.append(x)

   return hasil

C_skalar = skalar(A, 4)

def determinan(A):
   d1 = A[0][0] * A[1][1] * A[2][2] 
   d2 = A[0][1] * A[1][2] * A[2][0] 
   d3 = A[0][2] * A[1][0] * A[2][1] 

   d4 = A[0][2] * A[1][1] * A[2][0] 
   d5 = A[0][0] * A[1][2] * A[2][1] 
   d6 = A[0][1] * A[1][0] * A[2][2] 
   return (d1 + d2 + d3) - (d4 + d5 + d6)

det_A = determinan(A)
det_B = determinan(B)

print('A + B =')
for i in C_tambah:
   print(i)

print('\nA - B =')
for i in C_kurang:
   print(i)

print('\nA x 4 =')
for i in C_skalar:
   print(i)
   
print(f'\nDeterminan A = {det_A}')
print(f'\nDeterminan B = {det_B}')
