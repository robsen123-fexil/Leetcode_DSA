class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result=[]
        rw=len(img)
        cl=len(img[0])
       
        for i in range(len(img)):
            result.append([])
            for j in range(len(img[i])):
                sums=[]
                sums.append(img[i][j])
                if i-1>=0:
                    sums.append(img[i-1][j])
                    if j-1>=0:
                        sums.append(img[i-1][j-1])
                    if j+1<len(img[0]):
                        sums.append(img[i-1][j+1])
                if j-1>=0:
                    sums.append(img[i][j-1])
                if j+1<len(img[0]):
                    sums.append(img[i][j+1])
                if i+1<len(img):
                    k=i+1
                    sums.append(img[i+1][j])
                    if j-1>=0:
                        sums.append(img[i+1][j-1])
                    if j+1<len(img[k]):
                        sums.append(img[i+1][j+1])
                result[-1].append(math.floor(sum(sums) / len(sums)))
        return result
            