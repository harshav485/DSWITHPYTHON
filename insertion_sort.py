from operator import le


def insertion_sort(my_list):
    for i in range(len(my_list)):
        for j in range (i+1):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list


print(insertion_sort([4,2,6,5,1,3]))