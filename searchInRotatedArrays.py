class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        return self.binary_search(nums, target, 0, len(nums)-1)
    
    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = left + (right-left+1) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]:
            if nums[left] <= target and target < nums[mid]:
                return self.binary_search(nums, target, left, mid-1)
            else:
                return self.binary_search(nums, target, mid+1, right)
        else:
            if nums[mid] < target and target <= nums[right]:
                print("3")
                return self.binary_search(nums, target, mid+1, right)
            else:
                return self.binary_search(nums, target, left, mid-1)
