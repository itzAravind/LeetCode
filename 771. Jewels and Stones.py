class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map = {}
        result = 0
        for i in range(len(jewels)):
            if (jewels[i] in map):
                map[jewels[i]] = 1
            else:
                map[jewels[i]] = 1
        for i in range(len(stones)):
            if (stones[i] in map):
                result += 1
        return result