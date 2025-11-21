def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# --------- RUN & PRINT RESULTS ---------

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

print("Original nums:", nums)
print("Value to remove:", val)

k = removeElement(nums, val)

print("k (remaining elements):", k)
print("Modified nums:", nums)
print("First k valid elements:", nums[:k])
