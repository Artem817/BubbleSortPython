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


my_list1 = [64, 34, 25, 12, 22, 11, 91]

print(f"Initial list1:{my_list1}")

sorted_list1 = bubble_sort(my_list1)

print(f"Sorted list:{sorted_list1}")

my_list2 = [1, 5, 5, 2, 22, 11, 90]

print(f"Initial list:{my_list2}")

sorted_list2 = bubble_sort(my_list2)

print(f"Sorted list:{sorted_list2}")