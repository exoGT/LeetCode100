class Solution:
    def maxArea(self, height: List[int]) -> int:
        pts = []
        for x, y in enumerate(height):
            pts.append((x,y))

        left, right, ans = 0, len(pts)-1, 0

        while left < right:
            area = min(pts[left][1], pts[right][1])*abs(pts[left][0]-pts[right][0])
            if area > ans: ans = area
            if pts[left][1] < pts[right][1]:
                left += 1
            else: right -= 1

        return ans

