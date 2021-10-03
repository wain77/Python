def findMaxConsecutiveOnes(nums):
    onesCounter = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            onesCounter += 1
        if nums[i] == 0:
            onesCounter = 0
    
    return onesCounter

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))