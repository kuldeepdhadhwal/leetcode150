class Solution:
    
    def shortestCommonSupersequence(self, str1: str, str2: str, i=0,j=0,lookup =None)-> str:
        lookup = {} if lookup is None else lookup

        if (i,j) in lookup:
            return lookup[(i,j)]

        if i == len(str1):
            return len(str2) - j

        elif j == len(str2):
            return len(str1) - i

        elif str1[i] == str2[j]:
            lookup[(i,j)] =  1 + self.shortestCommonSupersequence(str1,str2,i+1,j+1,lookup)
            return lookup[(i,j)]
        
        else:
            lookup[(i,j)] =  1 + min(self.shortestCommonSupersequence(str1,str2,i+1,j,lookup), self.shortestCommonSupersequence(str1,str2,i,j+1,lookup))
            return lookup[(i,j)]
