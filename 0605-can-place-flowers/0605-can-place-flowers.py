class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def left(f , l):
           
            if l==0 or f[l-1]==0:
                return 'pass'
            else:
                return 'jump'
        def right(f , l):
            if l==len(f)-1 or f[l+1]==0:
                return 'pass'
            else:
                'jump'
        l=0
        while l<len(flowerbed):
            if flowerbed[l]==1:
                l+=1
            else:
                
                if left(flowerbed , l)=='pass' and right(flowerbed , l)=='pass':
                    n-=1
                    l+=2
                else:
                    l+=1
        print(n)
        return True if n<=0 else False
                
