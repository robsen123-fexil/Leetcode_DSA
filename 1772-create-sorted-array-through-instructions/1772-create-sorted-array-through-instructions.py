class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums =SortedList()
        count = 0
        MOD = 10**9 + 7
        for i in instructions:
            count += min(nums.bisect_left( i), len(nums)-nums.bisect_right(i))  
            nums.add(i)
           
        return count % MOD
