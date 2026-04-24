class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result:List[int]=[]
        for idx, number in enumerate(numbers):
            diff = target - number 
            if diff in numbers:
                idx_diff = numbers.index(diff)
                result += [idx+1,idx_diff+1]
                break
        return result

        