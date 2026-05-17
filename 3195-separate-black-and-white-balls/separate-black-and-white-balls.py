class Solution:
    def minimumSteps(self, s: str) -> int:

        swapL = 0
        swapR = 0
        swap = []

        length = len(s)

        for i in range(length):
            if s[i] == "0":
                swap.append(i)
        
        zeros = len(swap)

        for i in range(zeros):
            swapL += swap[i]-i
        
        ind = length-1
        for i in range(zeros-1,-1,-1):
            swapR+= ind - swap[i]
        # solution for finding minimum if 0's can be placed on either side
        return swapL
        