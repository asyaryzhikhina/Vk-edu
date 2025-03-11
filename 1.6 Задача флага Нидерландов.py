#Дан массив состоящий из нулей, единиц и двоек. Необходимо его отсортировать за линейное время.
def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while (mid <= high):
        if (nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            low+=1
            mid+=1
        elif (nums[mid] == 1):
            mid+=1
        elif (nums[mid] == 2):
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1
    return nums
