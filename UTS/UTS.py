#=== BAGIAN A===

DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
   """fungsi untuk menentukan pemenang"""
   
   if pilihan_pemain == pilihan_komputer:
      return 'seri'

   elif pilihan_pemain == 'kertas':
      if pilihan_komputer == 'gunting':
         return 'komputer'
      elif pilihan_komputer == 'batu':
         return 'pemain'

   elif pilihan_pemain == 'gunting':
      if pilihan_komputer == 'kertas':
         return 'pemain'
      elif pilihan_komputer == 'batu':
         return 'komputer'

   elif pilihan_pemain == 'batu':
      if pilihan_komputer == 'gunting':
         return 'pemain'
      elif pilihan_komputer == 'kertas':
         return 'komputer'

def main_satu_giliran(nomor_giliran):
   """fungsi untuk menginput pilihan pemain & melakukan satu giliran permainan"""

   pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]

   pilihan_pemain = input('\nMasukkan pilihan pemain (batu/gunting/kertas): ').lower()

   while pilihan_pemain not in DAFTAR_PILIHAN:
      print('pilihan tidak valid!!')

      pilihan_pemain = input('\nMasukkan ulang pilihan pemain (batu/kunting/kertas): ').lower()

   pemenang = tentukan_pemenang(pilihan_pemain, pilihan_komputer)

   if pemenang == 'seri':
      print(f'== Seri ==')
   
   else:
      print(f'== Pemenang : {pemenang} ==')
      print(f'pilihan pemain : {pilihan_pemain}')
      print(f'pilihan komputer : {pilihan_komputer}')

      return pemenang


def main_satu_ronde(nama):
   """fungsi untuk menentukan skor pemain dalam satu ronde permainan"""

   nomor_giliran = 1
   skor = 0
   pemain_win = 0
   komputer_win = 0

   while komputer_win != 3 and pemain_win != 3:
      hasil_giliran = main_satu_giliran(nomor_giliran)

      if hasil_giliran == 'pemain':
         pemain_win += 1
         skor += (nomor_giliran*10)

      elif hasil_giliran == 'komputer':
         komputer_win += 1

      nomor_giliran += 1

   return [nama, skor]


#=== BAGIAN B ===

def tampilkan_riwayat(riwayat):
   """fungsi untuk menampilkan riwayat dengan format tabel rapi"""
   if len(riwayat) == 0:
      print('\nBelum ada riwayat')

   print('\nNo |   Nama   | Skor')
   print('-'*18)
   for i in range(len(riwayat)):
      print(f'{i+1:<3}| {riwayat[i][0]:<9}| {riwayat[i][1]}')


#=== BAGIAN C ===

def bubble_sort_riwayat(riwayat):
   """fungsi untuk mengurutkan data riwayat (copy) dari skor tertinggi ke terendah"""

   data = riwayat.copy()
   n = len(data)

   for i in range(n-1):
      for j in range(n-1-i):
         if data[j][1] < data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]

   return data

def tampilkan_leaderboard(riwayat):
   """fungsi untuk menampilkan leaderboard"""

   tabel = bubble_sort_riwayat(riwayat)
   peringkat = 1

   print('\n= Leaderbord =')
   print('Peringkat |   Nama   | Skor')
   print('-'*25)

   for i,j in tabel:
      if peringkat == 1:
         print((f'    {peringkat:<6}| {i:<9}| {j} *'))
      else:
         print(f'    {peringkat:<6}| {i:<9}| {j}')

      peringkat += 1


#=== PROGRAM UTAMA ===
def main():
   """program utama game"""

   riwayat = []
   lanjut = True

   while lanjut:
      nama = input('\nMasukkan nama : ')
      hasil = main_satu_ronde(nama)

      riwayat.append(hasil)

      lanjut = True if input('\nmau lanjut main? (y/n): ').lower() == 'y' else False

   tampilkan_riwayat(riwayat)

   tampilkan_leaderboard(riwayat)

#=== JALANKAN GAME ===
main()
