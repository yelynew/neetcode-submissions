class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        closeOpen={"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in closeOpen:
                if stk and stk[-1]==closeOpen[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return False if stk else True
        
