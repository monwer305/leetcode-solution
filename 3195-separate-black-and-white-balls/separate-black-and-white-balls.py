class Solution:
    def minimumSteps(self, s: str) -> int:

        swapL = 0

        length = len(s)
        ind = 0
        for i in range(length):
            if s[i] == "0":
                swapL += i-ind
                ind+=1  

        return swapL
        