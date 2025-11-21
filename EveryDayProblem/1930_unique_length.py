class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        checker_ = set(s)
        middle_chars = 0
        for char in checker_:
            start, end = s.find(char), s.rfind(char)
            if end - start > 1:
                middle_chars = set(s[start+1:end])
                count += len(middle_chars)
        return count