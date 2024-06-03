from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if num in visited and visited[num] >= 1:
                return True
            visited[num] = visited.get(num, 0) + 1
