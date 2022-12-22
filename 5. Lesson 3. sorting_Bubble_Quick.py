
import time
import random

def bubble_sort(lst):
    upperCount = 1
    while upperCount <= len(lst) - 1:
        count = 1
        while count <= len(lst) - 1:
          #  print(f"Count is : {count} and UpperCount is {upperCount}")
            if lst[count-1] > lst [count]:
                temp = lst[count-1]
                lst[count - 1] = lst [count]
                lst[count] = temp
            count += 1
           # print(lst)
        upperCount +=1
    return lst

def quicksort(array):
    length = len(array)

    if length <= 1:
        return array
    else:
        pivot = array.pop()

    lower_lst = []
    higher_lst = []

    for item in array:
        if item < pivot:
            lower_lst.append(item)
        else:
            higher_lst.append(item)
    return quicksort(lower_lst) + [pivot] + quicksort(higher_lst)



lst = []

for i in range(1000):
    rand = random.randrange(1,100000)
    lst.append(rand)



startTime = time.time()
bubble_sort(lst)
print(f"The Bubble time duration is : {time.time() - startTime}")

startTime = time.time()
quicksort(lst)
print(f"The Quick sort time duration is : {time.time() - startTime}")

