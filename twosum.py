def twoSum(nums, target):
    hm = dict()

    for i, v in enumerate(nums):
        if target - v in hm:
            return [hm[target - v], i]
        else:
            hm[v] = i 

    return [-1, -1]


nums = [2, 7, 11, 15]
target = 18

print(twoSum(nums, target))