def rata_rata(nilai):
   if len(nilai) == 0:
      return 'data kosong'
   
   avg = 0
   for i in range(len(nilai)):
      avg += nilai[i]
   
   avg = avg / len(nilai)
   return avg

angka = [80, 75, 90, 60, 85]

print(f'rata-rata = {rata_rata(angka)}')