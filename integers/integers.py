def arraycheck(nums):
    for i in range(len (nums)-2):
        if nums[i]==1 and nums[i+1]==3:
            return True
    return False