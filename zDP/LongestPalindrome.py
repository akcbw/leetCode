"""
problems/longest-palindromic-substring/

"""

def longestPalindrome( s):
    stringLength = len(s)
    if stringLength == 0:
        return s
    dpTable = stringLength * [1]

    maxMidIndex = 0
    i = 0
    while i < stringLength:
        if i > 0:
            maxSubStringLength = 0
            detectRange = 1
            if i > stringLength // 2:
                detectRange = stringLength - i
            else:
                detectRange = i + 1
            for j in range(detectRange):
                if s[i - j ] == s[i + j]:
                    maxSubStringLength += 1
                else:
                    break
            if maxSubStringLength >= max(dpTable):
                maxMidIndex = i
            dpTable[i] = maxSubStringLength
            i = i + maxSubStringLength
        else:
            i+=1
    maxSubStringLength = max(dpTable)
    result = s[maxMidIndex + 1 - maxSubStringLength: maxMidIndex + maxSubStringLength]
    return result

if __name__ == '__main__':
    print(longestPalindrome('a'))

