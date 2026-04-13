class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for ch in s:
            if ch in m:
                pop_element = stack.pop() if stack else '#'
                if m[ch] != pop_element:
                    return False
            else:
                stack.append(ch)
        return not stack