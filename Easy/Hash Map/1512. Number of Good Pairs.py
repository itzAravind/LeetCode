class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        counter = 0
        for i in nums:
            if i in dict:
                counter += dict[i]
                dict[i] += 1
            else:
                dict[i] = 1
        return counter