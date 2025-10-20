import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    else:
        pivot = random.choice(arr)  
        left = [x for x in arr if x < pivot]   
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot] 
        
        return quick_sort(left) + middle + quick_sort(right)

my_list = [64, 34, 25, 12, 22, 11, 90]
print("Initial list:", my_list)
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)
