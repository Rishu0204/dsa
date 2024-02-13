class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX=2**31-1     #sets upper limit
        INT_MIN=-2**31      #sets lower limit
        
        if x==0:
            return 0
        sign=1 if x>0 else -1       #checks sign 1 if positive else -1
        x=abs(x)        #takes the absolute value of x 
        #reversing
        reverse=int(str(x)[::-1]) * sign        #reverse as str and return it to int and multiple with sign to return back its sign
        if reverse < INT_MIN or reverse>INT_MAX:     #checks the range of 'reverse' if out of range return 0
            return 0
        return reverse