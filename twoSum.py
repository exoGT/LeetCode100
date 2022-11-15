class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)): # 0 1 2 3
            hashmap[nums[i]] = i # {2:0, 7:1, 11:2, 15:3}
        for i in range(len(nums)): # 0 1 2 3
            complement = target - nums[i] # 9-2=7 9-7=2 9-11=-2 9-15=-6
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
