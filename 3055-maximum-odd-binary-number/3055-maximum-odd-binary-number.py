class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros=s.count('0')
        ones=s.count('1')
        strs='1'*(ones-1)+'0'*(zeros)+'1'
        return strs