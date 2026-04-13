class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False