def twoSum(nums,target):
    for i in range(len(nums)):
        diff = target - nums.pop(0)
        if diff in nums:
            return [i,nums.index(diff)+i+1]

inputNums = [2,11,15,7]
inputTarget = 9

print(twoSum(inputNums,inputTarget))
