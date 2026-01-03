class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            num = x
            rev = 0
            while num:
                last = num%10
                rev = rev*10 + last
                num = num//10
            if x == rev:
                return True
            return False
        else:
            return False