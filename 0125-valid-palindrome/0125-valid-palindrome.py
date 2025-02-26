class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        String = ''
        for i in s:
            if i.isalnum():
                String += i.lower()
        Rev = String[::-1]
        return Rev == String 