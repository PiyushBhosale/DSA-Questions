class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        ans = 0
        while num > 0:
            last = num%10
            ans = ans*10 + last
            num = num//10
        if ans.bit_length() > 31 or ans.bit_length() < -32:
            return 0
        return -ans if x < 0 else ans