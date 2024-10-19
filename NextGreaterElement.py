def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  
    
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
nums = [4, 5, 2, 25]
print(nextGreaterElements(nums))
