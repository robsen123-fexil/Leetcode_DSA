class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxima=0
        pref=[0]*(len(energy))
        if k>=len(energy):
            return max(energy)
        for i in range(k):
            pref[i]+=energy[i]
        print(pref)
        for i in range(k , len(pref)):
            print(pref[i] , pref[i-k+pref[i]])
            pref[i]=max(energy[i] , (pref[i-k]+energy[i]))
        print(pref)
        return max(pref[-k:])