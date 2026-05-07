struktur = {
   "Skripsi_Aqil": {
      "Bab_1": {
         "pendahuluan.docx": 45,
         "latar_belakang.docx": 62
      },
      "Bab_2": {
         "landasan_teori.docx": 118,
         "referensi": {
            "paper_A.pdf": 340,
            "paper_B.pdf": 210
         }
      },
      "Bab_3": {
         "metodologi.docx": 89,
         "diagram": {
            "flowchart.png": 512,
            "erd.png": 278,
            "arsitektur": {
               "sistem.png": 430
            }
         }
      },
      "sidang": {
         "presentasi.pptx": 2048,
         "catatan_revisi.txt": 15
      },
      "README.txt": 8
   }
}

def total_ukuran(folder, ukuran):
   key_folder = list(folder.items())

   for i, j in key_folder:
      if not isinstance(folder[i], dict):
         ukuran.append([i, j])
      else:
         total_ukuran(folder[i], ukuran)

def hitung_total(folder):
   global ukuran
   ukuran = []
   total_ukuran(folder, ukuran)

   return sum([j for i, j in ukuran]), len(ukuran)

def ambil_max(data):
   n = len(data)

   for i in range(n-1):
      for j in range(n-1-i):
         if data[j][1] < data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]

   return data[0]

def tampilkan_tree(folder, nama, level = 0):
   tab = '   '*level

   if isinstance(folder, dict):
      print(f'{tab}[] {nama}')

      for nama_isi, isi, in folder.items():
         tampilkan_tree(isi, nama_isi, level + 1)
   
   else:
      print(f'{tab}- {nama} ({folder} KB)')


ttl_ukr, jmlh_file = hitung_total(struktur)
print(f'Total ukuran skripsi: {ttl_ukr} KB')
print(f'Jumlah file: {jmlh_file} file')

file_terbesar = ambil_max(ukuran.copy())
print(f'File terbesar: {file_terbesar[0]} ({file_terbesar[1]} KB)\n')

tampilkan_tree(struktur['Skripsi_Aqil'], 'Skripsi_Aqil')