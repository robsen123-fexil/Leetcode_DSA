class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lists=[]
        for i in nums:
            lists.append(str(i))
        srted=sorted(lists , key=lambda x:x*10 , reverse=True)
        if ''.join(srted)[0]=='0':
            return '0'
        return ''.join(srted)