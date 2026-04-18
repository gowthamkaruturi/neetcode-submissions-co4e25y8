from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        left =0
        result=[]
       

        counter_map = Counter(nums) 
        count =0
        for key,value in counter_map.most_common(k):
            count +=1 
            result.append(key)
            if count == k:
                return result
        return result