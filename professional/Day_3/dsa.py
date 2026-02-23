# Pattern 1
def twosum(nums, target):
    seen = {}
    for i , num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = I
    return []

# Patter 2 Sliding window
def max_subarray(nums, k):
    window_sum = sum(num[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k] # slide window
        max_sum = max(max_sum, window_sum)
    return max_sum

