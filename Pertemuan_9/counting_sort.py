def counting_sort(data):
   counter = [0] * (max(data)+1)

   while len(data) > 0:
      index = data.pop(0)
      counter[index] += 1

   for i in range(len(counter)):
      while counter[i] > 0:
         data.append(i)
         counter[i] -= 1

   return data