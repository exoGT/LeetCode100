class Solution:
    def maxArea(self, height: List[int]) -> int:
        coordinates = []
        for x, y in enumerate(height):
            coordinates.append((y,x))
        coordinates.sort(reverse=True)

        area, ans = 0, 0

        for index in range(len(coordinates)-1):
            head = coordinates[index]

            for tup in coordinates[index:]:
                area = min(head[0], tup[0])*abs(head[1]-tup[1])
                if area > ans: ans = area
        
        return ans
