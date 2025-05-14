class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        lsts=bin(x^y).count('1')
        return lsts