class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0: return [nums]
        elif len(nums) == 3 and sum(nums) != 0: return []
        elif max(nums) == 0 and min(nums) == 0: return [[0,0,0]]

        hashmap = {}
        ans = []

        for target in nums: # -1 0 1 2 -1 -4
            tmplist = nums
            tmplist.pop(target) # [0,1,2,-1,-4] [-1,1,2,-1,-4]

            for i in range(len(tmplist)): # 0 1 2 3 4 
                    hashmap[tmplist[i]] = i # {0:0, 1:1, 2:2, -1:3, -4:4}            
                
                    for i in range(len(tmplist)): # 0 1 2 3 4 
                        complement = 0 - target - tmplist[i] # 1-0=1 1-1=0 1-2=-1 1-(-1)=1 1-(-4)=5

            if complement in hashmap and hashmap[complement] != i:
                res = [target, tmplist[i], complement]
                if sorted(res) not in ans:
                    ans.append(sorted(res))

        return ans


