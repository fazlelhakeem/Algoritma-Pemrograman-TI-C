def radix_sort(data):
   radixArray = [[], [], [], [], [], [], [], [], [], []]
   maxVal = max(data)
   exp = 1

   while maxVal // exp > 0:

      while len(data) > 0:
         val = data.pop()
         radixIndex = (val // exp) % 10
         radixArray[radixIndex].append(val)

      for bucket in radixArray:
         while len(bucket) > 0:
            val = bucket.pop()
            data.append(val)

      exp *= 10

   return data


def merge_sort(data):
   if len(data) <= 1:
      return data

   mid = len(data) // 2
   leftHalf = data[:mid]
   rightHalf = data[mid:]

   sortedLeft = merge_sort(leftHalf)
   sortedRight = merge_sort(rightHalf)

   return merge(sortedLeft, sortedRight)

def merge(left, right):
   result = []
   i = j = 0

   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1

   result.extend(left[i:])
   result.extend(right[j:])

   return result

def linear_search(data, angka):
   for i in range(len(data)):
      if data[i] == angka:
         print(f'{angka} ditemukan pada index ke {i}')
         return

   print('Tidak ada!!!')


def binary_search(data, angka):
   left = 0
   right = len(data) - 1

   while left <= right:
      mid = (left + right) // 2

      if data[mid] == angka:
         print(f'{angka} ditemukan pada index ke {mid}')
         return

      if data[mid] < angka:
         left = mid + 1
      else:
         right = mid - 1

   print('Tidak ada!!!')


data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

print('== Data Sebelum Diurutkan ==')
print(data)

print('\n== Data Setelah Dirutkan Dengan Radix Sort ==')
hasil_radix = radix_sort(data.copy())
print(hasil_radix)

print('\n== Data Setelah Dirutkan Dengan Merge Sort ==')
hasil_merge = merge_sort(data.copy())
print(hasil_merge)

angka = int(input('\nMasukkan angka yang ingin anda cari menggunakan linear search: '))
linear_search(hasil_radix, angka)

angka = int(input('\nMasukkan angka yang ingin anda cari menggunakan binary search: '))
binary_search(hasil_merge, angka)