'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
		# converts int into str
        convert_int = str(x)
        if convert_int == convert_int[::-1]:
            return True
        else:
            return False


# solution without converting ti string
import math 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return orig == back_x