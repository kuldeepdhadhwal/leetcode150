class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        my_dict = {"++X" : 1, "X++" : 1, "X--": -1 , "--X": -1}
        X = 0
        for opr in operations:
            if opr in my_dict:
                X += my_dict[opr]
        
        return X