class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def depthFirstSearch(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            depthFirstSearch(i, cur, total + candidates[i])
            cur.pop()
            depthFirstSearch(i + 1, cur, total)
        
        depthFirstSearch(0, [], 0)
        return ans
           
