class Solution:
    def isValid(self, s: str) -> bool:
        braces={')':'(','}':'{',']':'['}
        
        stk=[]
        
        for c in s:
            if c not in braces:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped_brace=stk.pop()
                    if popped_brace != braces[c]:
                        return False
        return not stk