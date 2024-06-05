from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for x in s:
            count[x] += 1

        for x in t:
            count[x] -= 1

        for num in count.values():
            if num != 0:
                return False

        return True
