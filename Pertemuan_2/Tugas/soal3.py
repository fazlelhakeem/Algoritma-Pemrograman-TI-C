def jumlah_digit(n):
   if n == 0:
      return 0
   else:
      return n%10 + jumlah_digit(n//10)

angka = int(input('masukkan angka : '))
print(f'Jumlah digit = {jumlah_digit(angka)}')