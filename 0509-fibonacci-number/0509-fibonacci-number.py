class Solution:
    def fib(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        return self.solve(n)

    def solve(self, n):
        if n <= 1:
            return n
        
        if self.dp[n] != -1:
            return self.dp[n]
        
        self.dp[n] = self.solve(n-1) + self.solve(n-2)
        return self.dp[n]