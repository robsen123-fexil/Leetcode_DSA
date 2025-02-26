class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        answer=pos_sum=neg_sum=0
        minimum_sum=maximum_sum=0
        for i in nums:
            pos_sum+=i
            pos_sum=max(pos_sum , 0)
            maximum_sum=max(maximum_sum , pos_sum)
            neg_sum+=i
            neg_sum=min(neg_sum , 0)
            minimum_sum=max(minimum_sum , -neg_sum)
            print(neg_sum , pos_sum)
        answer=max(maximum_sum , minimum_sum)
        return answer