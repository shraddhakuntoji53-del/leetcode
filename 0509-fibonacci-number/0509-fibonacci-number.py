class Solution:
    def fib(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        return self.fibo(n)

    def fibo(self, n):
        if n ==0 or n==1:
            return n
        
        if self.dp[n] != -1:
            return self.dp[n]
        
        self.dp[n] = self.fibo(n-1) + self.fibo(n-2)
        return self.dp[n]