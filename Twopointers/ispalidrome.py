class Solution:
    def isPalindrome(self, s: str) -> bool:
        upd_str = ''
        s = s.lower()
        if s == " " or s == "" or len(s)==1:
            return True
        
        for i in s:
            if i.isalnum():
                upd_str +=i
        left = 0
        right = len(upd_str) - 1
        while left < right:
            if upd_str[left] != upd_str[right]:
                return False
            left +=1
            right -=1
        return True