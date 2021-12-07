def nearestValue(nums, target):
    if len(nums) == 0: return 'Error'
    nums = list(nums)
    distancesToTarget = []
    for num in nums:
        distancesToTarget.append(abs(target - num))
    return nums[distancesToTarget.index(min(distancesToTarget))]
print(nearestValue({10, 11, 15, 17, 18, 20}, 13))
print(nearestValue({10, 11, 15, 17, 18, 20}, 19))
print(nearestValue({10, 11, 15, 17, 18, 20}, 14))