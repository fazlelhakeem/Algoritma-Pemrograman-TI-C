def pangkat_rekursif(a, b):
   if b == 0:
      return 1
   else:
      return a * pangkat_rekursif(a, b-1)

a = int(input('Masukkan angka : '))
b = int(input('Masukkan pangkat : '))

print(f'{a} pangkat {b} = {pangkat_rekursif(a, b)}')
