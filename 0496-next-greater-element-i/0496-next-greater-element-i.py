class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsh={}
        stack=[]
        frsts={}
        for i , val in enumerate(nums2):
            while stack and stack[-1]<val:
                b=stack.pop()
                frsts[b]=val
            stack.append(val)
        ans=[]
        for i in nums2:
            if i not in frsts:
                frsts[i]=-1
        for i in nums1:
            ans.append(frsts[i])
        return ans

