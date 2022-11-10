class Solution:
    def isHappy(self, n: int) -> bool:
        def checkHappy(n, counts):
            if n == 1:
                return True
            else:
                strint = str(n) 
                res = 0
                for i in range(len(strint)):
                    res += int(strint[i])**2
                if res in counts:
                    return False
                else:
                    counts[res] = 1
                    return checkHappy(res, counts)
        return checkHappy(n, {})
