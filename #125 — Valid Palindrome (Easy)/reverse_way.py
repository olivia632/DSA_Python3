class Solution:
    def isPalindrome(self,s:str)->bool:
        s=s.lower()
        newstring=""
        for char in s:
            if char.isalnum():
                newstring+=char
        return newstring == newstring[::-1]