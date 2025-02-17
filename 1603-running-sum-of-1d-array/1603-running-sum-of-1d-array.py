class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        sms=0
        for i in nums:
            sms+=i
            result.append(sms)
        return result
