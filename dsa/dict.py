# Simple dictionary
def build_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Dict with get()
def build_freq_map(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) +1
    return freq

# Defaultdict
from collections import defaultdict

def build_freq(arr):
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    return dict(freq)

# Counter
from collections import Counter
arr = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
freq = Counter(arr)

print(freq)

# find uniq char
def UniqChar(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1
    