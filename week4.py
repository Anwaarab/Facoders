def add_to_list(list_num,x):
    list2=[]
    for i in list_num:
        i=i+x
        list2.append(i)
    return list2
list1 = [10, 5, 2, 6, 9, 11, 23]
print(add_to_list(list1,2))
