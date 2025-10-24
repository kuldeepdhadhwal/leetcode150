class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from collections import Counter
        def is_balanced(x):
            count = Counter(str(x))
            for key, val in count.items():
                if int(key) != val:
                    return False
            return True


        m = n + 1
        while True:
            if is_balanced(m):
                print(m)
                return m
            m +=1
