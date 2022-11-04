class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack, tStack = [], []

        for i in range(len(s)):
            if sStack:
                if s[i] == "#":
                    sStack.pop()
                else:
                    sStack.append(s[i])
            else: 
                if s[i] != "#":
                    sStack.append(s[i])

        for j in range(len(t)):
            if tStack:
                if t[j] == "#":
                    tStack.pop()
                else:
                    tStack.append(t[j])
            else: 
                if t[j] != "#":
                    tStack.append(t[j])

        return sStack == tStack
        # Time: O(n)
        # Space: O(n)
