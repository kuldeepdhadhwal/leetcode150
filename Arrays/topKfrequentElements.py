class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []
        for i in nums:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        sorted_items = sorted(counter.items(),key=lambda x:x[1], reverse=True)
        print(sorted_items)
        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res
