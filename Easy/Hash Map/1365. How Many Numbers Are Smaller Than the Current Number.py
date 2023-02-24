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
    
"""This is a Python solution to the problem of finding the number of elements in a list that are smaller than the current element. The input is a list of integers "nums", and the output is a list of integers "result" where each element "result[i]" represents the number of elements in "nums" that are smaller than "nums[i]".

The solution works by first creating a dictionary "dict" that maps each unique element in "nums" to its index in the sorted."""

"""Overall time complexity is O(n log n) due to the sorting step, where "n" is the length of the input list "nums". The space complexity is O(n) because we create a dictionary with at most "n" key-value pairs. Note that the time complexity of dictionary lookups is expected O(1), which means on average it takes constant time to look up a key in a dictionary."""
