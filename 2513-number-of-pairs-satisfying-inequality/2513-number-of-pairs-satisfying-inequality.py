class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        lsts=SortedList()
        cnt=0
        for i in range(len(nums1)):
            cnt+=(lsts.bisect_right(nums1[i]-nums2[i]+diff))
            lsts.add(nums1[i]-nums2[i])
        return cnt
        