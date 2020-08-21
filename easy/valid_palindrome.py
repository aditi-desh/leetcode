'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(a for a in s if a.isalpha() or a.isdigit()).lower()
        rev_x = x[::-1]
        if x == rev_x:
            return True
        else:
            return False