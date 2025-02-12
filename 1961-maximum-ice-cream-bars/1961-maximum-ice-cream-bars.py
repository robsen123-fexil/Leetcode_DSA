class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        ls=[0]*(max(costs)+1)
        for i in costs:
            ls[i]+=1
        count=0
        print(ls)
        for i  , val in enumerate(ls):
            if (val*i)<=coins:
                count+=val
                coins-=(val*i)
                
            else:
                while coins>=(i):
                    count+=1
                    coins-=i
        return count
