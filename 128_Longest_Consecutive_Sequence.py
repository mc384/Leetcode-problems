class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        numbers = set()
        res = 0

        for num in nums:
            numbers.add(num)

        for num in numbers:
            if num - 1 not in numbers:
                cur = 1
                seq = num + 1
                while True:
                    if seq in numbers:
                        cur += 1
                        seq += 1
                    else:
                        break
                res = max(res, cur)
        return res 
