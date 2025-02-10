class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles
        while numBottles>=numExchange:
            mod=numBottles%numExchange
            numBottles//=numExchange
            result+=numBottles
            numBottles+=mod
            
           
        return result


