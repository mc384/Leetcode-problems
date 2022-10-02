class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [i for i in range(1, n+1)]
        j = 0
        while j < n:
            if res[j] % 3 == 0 and res[j] % 5 == 0:
                res[j] = "FizzBuzz"
                j += 1
            elif res[j] % 3 == 0:
                res[j] = "Fizz"
                j += 1 
            elif res[j] % 5 == 0:
                res[j] = "Buzz"
                j += 1
            else:
                res[j] = str(res[j])
                j += 1
        return res
