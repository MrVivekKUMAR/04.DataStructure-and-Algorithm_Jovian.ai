def rotationList_Linier(lst):
    if len(lst)<2:
        return 0

    position =0
    while position < len(lst)-1:
        if(lst[position] > lst[position+1]):
            return (position + 1)
        position += 1


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) -1

    while True:
        mid = (hi + lo) //2
        mid_number = nums[mid]

        # lst = [ _, 25_, 29, 3]
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        #lst = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
       # lo: 2, hi: 3, mid: 2, mid_number: 29

        if mid > 0 and mid_number < nums[mid-1] :
            # The middle position is the answer
            return mid

        elif mid_number < nums[hi] :
            # Answer lies in the left half
            hi = mid - 1

        else:
            # Answer lies in the right half
            lo = mid + 1

    return -1

# 1. List has 7 element (order), and rotated 3 time
# lst = [0 , 2, 3, 4 , 5, 6, 9, 10]
# lst = [5, 6, 9, 10 , 0 , 2, 3, 4]
# lst = [10 ,0 , 2, 3, 4 , 5, 6, 9]
# lst = [2, 3, 4 , 5,6 , 9, 10 ,0 ]


lst = [19, 25, 29, 3, 5, 6, 7, 9, 11,14]

print(rotationList_Linier(lst))
print(count_rotations_binary(lst))

# 2. List has 10 element (Even) , adn rotate 3 time
# 3. List rotated N Times, where N is number of element. o/p = 0
# 4. List rotated (N-1) Times, where N is number of element. o/p = N-1
# 5. List given is empty o/p = 0
# 6. List may have negative number and positive number mix rotated 5 times

