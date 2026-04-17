#INSERTION SORT
def insertion_sort(data):
   n = len(data)
   
   for i in range(1,n):
      insert_index = i
      current_value = data[i]
      
      for j in range(i-1, -1, -1):
         if data[j] > current_value:
            data[j+1] = data[j]
            insert_index = j
         else:
            break

      data[insert_index] = current_value

def partition(data, low, high):
   pivot = data[high]
   i = low - 1

   for j in range(low, high):
      if data[j] <= pivot:
         i += 1
         data[i], data[j] = data[j], data[i]

   data[i+1], data[high] = data[high], data[i+1]
   return i+1

#QUICK SORT
def quicksort(data, low=0, high=None):
   if high is None:
      high = len(data) - 1

   if low < high:
      pivot_index = partition(data, low, high)
      quicksort(data, low, pivot_index-1)
      quicksort(data, pivot_index+1, high)


#COUNTING SORT
def counting_sort(data):
   max_val = max(data)
   count = [0] * (max_val + 1)

   while len(data) > 0:
      num = data.pop(0)
      count[num] += 1

   for i in range(len(count)):
      while count[i] > 0:
         data.append(i)
         count[i] -= 1

   return data


index = int(input('Masukkan jumlah elemen yang ingin dimasukkan : '))

data= []

for i in range(index):
   elemen = int(input(f'masukkan elemen indeks ke-{i+1} : '))

   while elemen < 0:
      print('\nelemen yang anda masukkan tidak valid!!')
      elemen = int(input(f'masukkan elemen indeks ke-{i+1} : '))
      

   data.append(elemen)


print('\n== DATA SEBELUM DIURUTKAN ==')
print(', '.join([str(x) for x in data]))

data01 = data.copy()
data02 = data.copy()

insertion_sort(data01)
quicksort(data02)

print('\n== DATA SETELAH DIURUTKAN PAKAI INSERTION SORT ==')
print(', '.join([str(x) for x in data01]))

print('\n== DATA SETELAH DIURUTKAN PAKAI QUICK SORT ==')
print(', '.join([str(x) for x in data02]))

print('\n== DATA SETELAH DIURUTKAN PAKAI COUNTING SORT ==')
print(', '.join([str(x) for x in counting_sort(data)]))