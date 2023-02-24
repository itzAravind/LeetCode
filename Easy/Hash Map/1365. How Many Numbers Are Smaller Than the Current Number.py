class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]] = i
        for j in nums:
            result.append(dict[j])
        return result