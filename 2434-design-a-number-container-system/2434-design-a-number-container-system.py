class NumberContainers:

    def __init__(self):
        self.hsh=defaultdict(list)
        self.lists={}
        

    def change(self, index: int, number: int) -> None:
        if index in self.lists:
            val=self.lists[index]
            self.lists[index]=number
            
            self.hsh[val].remove(index)
            if not self.hsh[val]:
                del self.hsh[val]
            
        self.lists[index]=number
        bisect.insort(self.hsh[number], index)
        
        

    def find(self, number: int) -> int:
        return (self.hsh[number][0]) if self.hsh[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)