class Solution:
    def largest(self, arr):
    # Initialize maximum element
      max = arr[0]
      for num in arr:
        if num > max:
            max = num
      return max
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0,len(nums)-k+1):
          res.append(self.largest(nums[i:i+k]) )  
        return res
        