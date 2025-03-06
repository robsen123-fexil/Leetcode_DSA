class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsh={}
        stack=[]
        frsts=defaultdict(int)
        for i , val in enumerate(nums2):
            while stack and stack[-1]<val:
                b=stack.pop()
                frsts[b]=val
            stack.append(val)
        ans=[]
        for i in nums1:
            if not frsts[i]:
                ans.append(-1)
            else:
                ans.append(frsts[i])
        return ans