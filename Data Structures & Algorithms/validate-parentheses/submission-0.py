

class Solution:
     def isValid(self, s:str) -> bool:
        _stack = []
        
        for letter in s:
            if letter in ["{","(","["]:
                _stack.append(letter)
            elif len(_stack)>0:
                if letter == "}":
                    if _stack.pop() != "{":
                        return False
                if letter == ")":
                    if _stack.pop() != "(":
                        return False
                if letter == "]":
                    if _stack.pop() != "[":
                        return False
            else:
                return False
        return len(_stack) ==0 
        