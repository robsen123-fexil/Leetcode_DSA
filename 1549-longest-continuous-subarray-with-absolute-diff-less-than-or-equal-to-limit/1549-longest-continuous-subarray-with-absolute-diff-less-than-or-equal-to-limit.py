class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_ques=deque()
        max_ques=deque()
        r=l=maxi=0

        while r<len(nums):
            while min_ques and min_ques[-1]>nums[r]:
                min_ques.pop()
            while max_ques and max_ques[-1]<nums[r]:
                max_ques.pop()
            
            max_ques.append(nums[r])
            min_ques.append(nums[r])
            
            while max_ques[0]-min_ques[0]>limit:
                if nums[l]==min_ques[0]:
                    min_ques.popleft()
                if nums[l]==max_ques[0]:
                    max_ques.popleft()
                l+=1
            
            maxi=max(maxi , r-l+1)
            r+=1
        return maxi