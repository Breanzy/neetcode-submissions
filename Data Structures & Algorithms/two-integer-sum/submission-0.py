class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}
        
        for n in range(len(nums)):
            if (target - nums[n]) in numsHash:
                return [numsHash[target - nums[n]], n]
            numsHash[nums[n]] = n