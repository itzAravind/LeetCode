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
 """This code defines a class named Solution with a method named smallerNumbersThanCurrent. This method takes a list of integers nums as input and returns a list of integers.

The first line of the method creates an empty dictionary named dict.

The second line sorts the input list nums in ascending order and assigns it to a new variable named sorted_nums.

The next for loop iterates through the sorted list sorted_nums and checks if each number in the list is not already in the dict. If it's not in the dictionary, the code adds it as a key to the dictionary and assigns its index in the sorted list as its value.

Finally, the code uses another for loop to iterate through the original input list nums and appends the count of smaller numbers than the current number in the result list. The count is obtained by looking up the value of the current number in the dict.

So the overall functionality of this code is to return a list of counts, where each count represents the number of elements in the input list that are smaller than the corresponding element at the same index in the input list."""
