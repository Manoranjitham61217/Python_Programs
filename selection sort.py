def selection_sort(arr):

  for i in range(len(arr)):
       min= i
       for j in range(i+1, len(arr)):
           if arr[min] > arr[j]:
               min = j
       temp=arr[min]
       arr[min]=arr[i]
       arr[i]=temp

my_array = [64, 25, 12, 22, 11, 90]
selection_sort(my_array)
print(my_array)
