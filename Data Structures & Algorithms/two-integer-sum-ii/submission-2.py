class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right =0, len(numbers)-1
        for n in numbers:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum > target:
                right= right -1
            else:
                left = left +1
        return []
