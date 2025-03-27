class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        maxi=max(cnt , key=cnt.get)
       
        l=0
   
        count=0
        while l<len(nums):
            if nums[l]==maxi:
                count+=1
            if (count*2)>(l+1):
                break
            l+=1
        print(l)
       
        def righter(l , maxi):
            count=0
            r=len(nums)-1
            
            while r>l:
                if nums[r]==maxi:
                    count+=1
                r-=1
            print(len(nums)-(r+1) , count)
            if (count*2)>(len(nums)-(r+1)):
                return True
            return False
        if righter(l ,maxi):
            return l
        return False-1