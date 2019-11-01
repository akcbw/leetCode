class Solution:
    process = []
    def pancakeSort(self,cakes):
        if (cakes == sorted(cakes)):
            return self.process
        maxCakeIndex = 0
        maxCakeSize = 0
        for i in range(len(cakes)):
            if cakes[i] > maxCakeSize:
                maxCakeSize = cakes[i]
                maxCakeIndex = i
        if maxCakeIndex > 0:
            cakes = cakes[:maxCakeIndex + 1][::-1] + cakes[maxCakeIndex + 1:]
            self.process.append(maxCakeIndex + 1)
        cakes = cakes[::-1]
        self.process.append(len(cakes))
        return self.pancakeSort(cakes[:-1])

s = Solution()
print(s.pancakeSort([1,2,3]))