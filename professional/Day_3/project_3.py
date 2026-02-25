"""
Task:
Implement a sliding window algorithm Used in time-series feature engineering — 
find the max/sum in a sliding window of size K efficiently
"""

"""
Pseudo-code
if k invalid: error
window_sum = sum of first k elements
output window_sum
for i from k to n-1:
    window_sum += x[i] add new right element
    window_sum -= x[i-k] remove old left element
    output window_sum
"""
from typing import List

def sliding_window_sum(nums: List[float], k: int) -> List[float]:
    """ 
    Return rolling sum for every window of size k.
    Time: O(n)
    Space: O(1) extra excluding output
    """
    n = len(nums)
    # Validate inputs
    if k <= 0:
        raise ValueError("k must be >= 1")
    if k > n:
        return []

    # Build the first window sum
    window_sum = sum(nums[:k])

    # Store result for first window
    result : List[float] = [window_sum]

    # Slide the window from left to the right
    for right in range(k, n):
        # right is new element entering the window
        window_sum += nums[right]

        # left the element leaving the window
        left = right - k 
        window_sum -= nums[left]

        result.append(window_sum)
    return result

# Sliding window Max in  O(n) using a Monotonic Deque
"""
deque = empty
for i in [0..n-1]:
    #remove indices outside window(i-k)
    while deque front < i-k=1:
        pop left
    # maintain decreasing order
    while deque not empty and nums[ deque back] <= nums[i]:
        pop back
    # push current index
    push back i 
    # start recording results when first window complete
    if i >= k-1:
        output nums[deque front]
    """

from collection import deque
from typing import List

def sliding_window_sum(nums: List[float], k: int) -> List[float]:
    """
    Return rolling maximum for every window of size k.
    Time: O(n)
    Space: O(k)
    """
    n = len(nums)
    if k <= 0:
        raise ValueError("k must be > 1")
    if k > n:
        return []

    dq = deque() # stories indices, nums[dq] is decreasing
    result: List[float] = []
    for right in range(k, n):
        window_start = i - k + 1
        if dq and dq[0] < window_start:
            dq.popleft()
        
        # Maintain decreasing order in deque
        # Remove smaller (or equal) values from the back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Record max once the first window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result 

