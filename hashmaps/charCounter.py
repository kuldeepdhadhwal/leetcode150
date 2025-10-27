class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        charCount = Counter(magazine)
        print(charCount)
        for i in ransomNote:
            if i in charCount and charCount[i] > 0:
                charCount[i] -=1
            else:
                return False
        return True