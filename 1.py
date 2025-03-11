# ТЗ: Дан массив целых чисел. Необходимо развернуть его. Сделать это надо за линейное время без дополнительных аллокаций памяти
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [] 
