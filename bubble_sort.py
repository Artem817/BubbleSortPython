def bubble_sort(data_list):
    n = len(data_list)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if data_list[i - 1] > data_list[i]:
                data_list[i - 1], data_list[i] = data_list[i], data_list[i - 1]
                new_n = i  
        n = new_n  
    return data_list


my_list = [64, 34, 25, 12, 22, 11, 90]

print(f"Initial list:{my_list}")

sorted_list = bubble_sort(my_list)

print(f"Sorted list:{sorted_list}")
