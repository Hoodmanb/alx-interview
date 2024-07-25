#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    def list_generator(previous):
        newList = [1]
        for index, value in enumerate(previous[:-1]):
            next_ = previous[index + 1]
            sum_value = value + next_
            newList.append(sum_value)
        newList.append(1)
        return newList
    
    lists = []
    list_ = [1]
    for i in range(n):
        lists.append(list_)
        list_ = list_generator(list_)
    
    return lists
