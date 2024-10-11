def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

my_array = [64, 25, 12, 22, 11, 90]
insertion_sort(my_array)
print(my_array)
