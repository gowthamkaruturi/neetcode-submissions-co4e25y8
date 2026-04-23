class Solution:

    def encode(self, strs: List[str]) -> str:
       
        delim = '#'
        esc = '\\'
        encoded_string = ""

        for string in strs:
            for ch in string:
                if ch == delim or ch == esc:
                    encoded_string += esc
                encoded_string += ch
            encoded_string += delim

        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        current = []
        delim ='#'
        esc = '\\'
        i = 0
        n = len(s)

        while i < n:
            if s[i] == esc and i+1 <n :
                current.append(s[i+1])
                i+=2
            elif s[i] == delim:
                res.append("".join(current))
                current = []
                i +=1
            else:
                current.append(s[i])
                i +=1
        if current:
            res.append("".join(current))        
        return res
