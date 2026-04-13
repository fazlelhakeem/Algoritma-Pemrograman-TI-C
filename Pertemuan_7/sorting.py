data = [2, 3, 6, 2, 8, 0]


def bubble(data):
   lst = data.copy()
   n = len(lst)
   pindah = 0

   for i in range(n-1):
      swapped = False
      for j in range(n-i-1):
         if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            pindah += 1
            swapped = True

      if not swapped:
         break

   return (lst, pindah)

def select(data):
   lst = data.copy()
   n = len(lst)
   pindah = 0

   for i in range(n):
      maks = i
      for j in range(i+1, n):
         if lst[j] > lst[maks]:
            maks = j

      if maks != i:
         lst[maks], lst[i] = lst[i], lst[maks]
         print(lst)
         pindah += 1

   return (lst, pindah)

buble_sort, pindah = bubble(data)
selestion_sort, hasil_pindah = select(data)

print('Bubble sort (kecil -> besar) :', buble_sort)
print('jumlah swap bubble sort :', pindah)

print('\nSelection sort (besar -> kecil) :', selestion_sort)
print('jumlah swap selection sort :', hasil_pindah)
