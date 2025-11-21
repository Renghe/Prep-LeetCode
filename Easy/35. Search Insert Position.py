def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left   # insert position


# ----------- RUN & PRINT ---------------

nums = [1, 3, 5, 6]
target = 5   # change this to test different cases

print("Nums:", nums)
print("Target:", target)

result = searchInsert(nums, target)

print("Output Index:", result)
