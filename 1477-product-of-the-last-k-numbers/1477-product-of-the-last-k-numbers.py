class ProductOfNumbers:

    def __init__(self):
        self.lists=[]
        self.ans = [1]
        

    def add(self, num: int) -> None:
        self.lists.append(num)
        if num == 0:
            self.ans = [1]
        else:
            self.ans.append(self.ans[-1] * num)
        
 
    def getProduct(self, k: int) -> int:
        dv=(k+1)
        return self.ans[-1]//self.ans[-dv] if k<(len(self.ans)) else 0 
            
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)