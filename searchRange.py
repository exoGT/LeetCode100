class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        
        def getIndex(nums: List[int], target: int) -> int:
            low, high, ans = 0, len(nums) - 1, []
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target: return mid                
                elif nums[mid] < target: low = mid + 1
                else: high = mid - 1

        def beGreedy(pos: int, nums: List[int], target: int) -> List[int]:
            left, right = pos, pos
            if pos is None or len(nums) == 0:
                return -1, -1
            elif pos == 0 and len(nums) == 1:
                return 0, 0
            else:
                while left - 1 >= 0 and nums[left - 1] == target: left -= 1 
                while right + 1 < len(nums) and nums[right + 1] == target: right += 1 
                return left, right

        return beGreedy(getIndex(nums, target), nums, target)
        
