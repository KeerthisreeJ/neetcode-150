class Solution:
    def isValid(self, s: str) -> bool:
        b = {'(':')', '{':'}', '[':']'}
        op = ['(', '{', '[']
        x = []
        for i in s :
            if i in op:
                x.append(i)
            else:
                if len(x) > 0 :
                    if i == b[x[-1]]:
                        x.pop()
                    else :
                        return False
                else :
                    return False 
        if len(x) == 0 :
            return True
        else : return False



        