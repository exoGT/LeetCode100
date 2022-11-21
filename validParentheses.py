class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for char in s:
            if char in map:
                stack.append(char) # ['('] - ['(']
            elif not stack or map[stack[-1]]!=char:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0  
