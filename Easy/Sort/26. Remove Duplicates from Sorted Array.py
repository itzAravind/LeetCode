class Solution:
    def removeDuplicates(self, nums: List[int], k = 1) -> int:
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:            # detect next unique value
                nums[k] = nums[i]               # move it to the end of deduplicated array
                k += 1                          # update the size of deduplicated array
        return k
    
 """This code defines a class "Solution" that has a method "removeDuplicates". The method takes in an array of integers "nums" and an optional parameter "k" with a default value of 1. The purpose of the method is to remove duplicates from the "nums" array and return the size of the resulting deduplicated array.

The method iterates through the "nums" array using a for loop starting from the second element. It compares the current element with the previous element to detect the next unique value. When a unique value is found, it is moved to the end of the deduplicated array by assigning it to the element at index "k". The size of the deduplicated array is updated by incrementing the "k" variable.

Finally, the method returns the size of the deduplicated array.

Overall, this code effectively removes duplicates from an array in linear time (O(n)) and constant space (O(1)) by modifying the input array in-place. The optional parameter "k" allows the method to remove duplicates up to "k" times, which may be useful in certain scenarios."""
