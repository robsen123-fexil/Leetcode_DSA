class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        val=abs(z-y)-abs(z-x)
        if not val:
            return 0
        elif val<0:
            return 2
        else:
            return 1
