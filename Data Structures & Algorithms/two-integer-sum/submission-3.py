class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i , n in enumerate(nums):
            diff = target - n

            if diff in seen_dict:
                return [seen_dict[diff], i]
            seen_dict[n]=i
        