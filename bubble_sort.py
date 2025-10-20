def bubble_sort(data_list):
    n = len(data_list)
    
    for i in range(n):
        swapped = False 
        
        for j in range(0, n - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
        
        if not swapped:
            break
            
    return data_list

my_list = [64, 34, 25, 12, 22, 11, 90]

print(f"Initial list:{my_list}")

sorted_list = bubble_sort(my_list)

print(f"Sorted list:{sorted_list}")
