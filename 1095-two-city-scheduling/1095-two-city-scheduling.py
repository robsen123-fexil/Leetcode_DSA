class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0]-x[1]))
        leng=len(costs)//2
        print(costs)
        sums=0
        for i in range(0 , leng):
            sums+=costs[i][0]
        for i in range(leng , len(costs)):
            sums+=costs[i][1]
        return sums
        