class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for s in strs:
            res += s +"å"

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        current = ""
        for ch in s:
            if ch == "å":
                result.append(current) 
                current = ""
            else:
                current += ch
       
        return result
