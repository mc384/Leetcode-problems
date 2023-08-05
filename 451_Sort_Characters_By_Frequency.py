class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        heap = []

        for char in counts:
            heappush(heap, [counts[char]*-1, char])

        res = ""
        while heap:
            freq = heap[0][0]*-1
            res += heappop(heap)[1]*freq
        return res
