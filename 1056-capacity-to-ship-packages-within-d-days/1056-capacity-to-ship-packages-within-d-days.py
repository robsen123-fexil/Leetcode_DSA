from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        mini = float('inf')  

        def checker(mid):
            sums, count = 0, 1  
            for w in weights:
                if sums + w > mid:
                    count += 1
                    sums = 0 
                sums += w
            return count

        while left <= right:
            mid = (left + right) // 2
            count = checker(mid)
            if count <= days: 
                mini = min(mini, mid)
                right = mid - 1
            else: 
                left = mid + 1

        return mini
