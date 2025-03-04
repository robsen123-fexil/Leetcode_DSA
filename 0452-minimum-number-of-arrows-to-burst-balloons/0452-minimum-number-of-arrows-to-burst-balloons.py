class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count=0
        points.sort(key=lambda x:x[1])
        l=r=0
        print(points)
        while l<len(points):
            while r<len(points) and points[l][1]>=points[r][0]:
                r+=1
            l=r
            count+=1
        return count
            


        