class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort();
        max = 0;
          
        for x in range(0, int(len(nums)/2)):
              if max < nums[x] + nums[-x-1]: 
                    max = nums[x] + nums[-x-1]
        
        return max;