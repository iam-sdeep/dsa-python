def sumRange(nums, l, r):
    prefixSum = [0] * (len(nums) + 1)

    for i, val in enumerate(nums):
        prefixSum[i + 1] = prefixSum[i] + val

    return prefixSum[r] - prefixSum[l - 1] 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l, r = 2, 3

print(sumRange(nums, l, r))