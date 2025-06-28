
def zeroshift(nums):
    current_element = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[current_element]
            nums[current_element] = nums[i]
            nums[i] = temp
            current_element += 1
    return nums

nums = [1, 0, 0, 2, 1, 0]
result = zeroshift(nums)
print(result)
