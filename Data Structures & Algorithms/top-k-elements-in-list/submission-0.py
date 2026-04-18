from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        left =0
        result=[]
        if len(nums)<=0:
            return result

        counter_map = Counter(nums) 
        for key,value in counter_map.items():
            if value >=k:
                result.append(key)
        return result 
            