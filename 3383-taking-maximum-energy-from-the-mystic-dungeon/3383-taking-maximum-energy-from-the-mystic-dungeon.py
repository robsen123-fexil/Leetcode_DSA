class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxima=0
        pref=[0]*(len(energy))
        if k>=len(energy):
            return max(energy)
        for i in range(k):
            pref[i]+=energy[i]
      
        for i in range(k , len(pref)):
            
            pref[i]=max(energy[i] , (pref[i-k]+energy[i]))
        
        return max(pref[-k:])