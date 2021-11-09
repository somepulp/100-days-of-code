nums = [1, 7, 3, 6, 5, 6]

index = 1 
left_list = [1]
right_list = [3,6,5,6]



index = 2
left_list = [1,7]
right_list = [6,5,6]


sum_left = 0
sum_right = 0
#final_index = -1 
def pivot_index(num_lst):    
    list_left = []
    list_right = []
    for index in range(len(num_lst)):
        # if index == 0:
            # for i in len(nums):
        list_left.append(sum(num_lst[:index]))
        list_right.append(sum(num_lst[index+1:]))   # sum_right += nums[i+1]
        #check if sum are equal
        final_index = index if list_left[index]==list_right[index] else -1
        if final_index != -1:
            #print(final_index)
            break
    return(final_index)
        # else:
    #     for i in len(nums):
    #         sum_left += nums[index - i]
    #         sum_right += nums[index+1]
    #     print(sum_left)
    #     print(sum_right)
        #sum_left = 0
        #sum_right
    #sum_left = 0 if index <= 0 else 