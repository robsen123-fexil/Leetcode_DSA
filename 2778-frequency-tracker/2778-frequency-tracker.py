class FrequencyTracker:

    def __init__(self):
        self.cnt=Counter()
        self.frq=Counter()
        

    def add(self, number: int) -> None:
        value=self.cnt[number]
        
       
        if self.frq[value]:
            self.frq[value]-=1
            if self.frq[value]==0:
                self.frq.pop(value)

      

        self.cnt[number]+=1
        self.frq[self.cnt[number]]+=1
        

    def deleteOne(self, number: int) -> None:
        if self.cnt[number]:
            self.frq[self.cnt[number]]-=1
            if self.frq[self.cnt[number]]==0:
                del self.frq[self.cnt[number]]
            self.cnt[number]-=1
            if self.cnt[number]==0:
                self.cnt.pop(number)
            self.frq[self.cnt[number]]+=1
        




           
        

    def hasFrequency(self, frequency: int) -> bool:
        return True if frequency in self.frq else False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)