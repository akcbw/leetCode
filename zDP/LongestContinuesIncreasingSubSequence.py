'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

'''

def findLengthOfLCIS(seq):
    if not seq:
        return 0
    else:
        seqLength = len(seq)
        dpTable = seqLength * [1]
        n = 0
        while n < seqLength:
            i = 1
            while i < seqLength - n:
                if seq[n+i] > seq[n+i-1]:
                    i += 1
                else:
                    break
            dpTable[n] = i
            n = n + i
        return max(dpTable)

if __name__ == '__main__':
    print(findLengthOfLCIS([1,4,5,4,1,7,9]))