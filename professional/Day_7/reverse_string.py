def reverseString(s: list[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverseString_stack(s: list[str]) -> None:
    stack = []

    for char in s:
        stack.append(char)

    for i in range(len(s)):
        s[i] = stack.pop()

def reverseString_recursive(s: list[str]) -> None:
    def helper(left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        helper(left + 1, right - 1)
    helper(0, len(s) - 1)