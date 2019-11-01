class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        numLength = len(nums)
        dpResultTable = numLength * [0]
        for k in range(numLength):
            maxNum = nums[k]
            sum = nums[k]
            for j in range(k+1, numLength):
                sum = sum + nums[j]
                if nums[j] >= 0 and sum >= maxNum:
                    maxNum = sum
            dpResultTable[k] = maxNum
        return max(dpResultTable)

s = Solution()
print(s.maxSubArray([1,2]))