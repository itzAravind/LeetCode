class Solution:
    def maximumCount(self, nums: List[int]) -> int: # nums = [-3,-2,-1,0,0,1,2]
        total_len = len(nums)
        neg, pos = 0, 0
        zero_found = False
        if nums[-1] < 0 : # if the last digit is negative, we can simply return the total length of list
            return total_len

        for i in range(total_len):
            if nums[i] > 0 : # when i == 5
                pos = total_len - i # pos = 7 - 5 = 2
                if neg == 0: # neg is not zero, neg = 3 when i was 3
                    neg = i
                break
            if nums[i] == 0 and not zero_found: # when i = 3
                neg, zero_found = i, True # neg = 3 and zero_found = True
        return max(neg, pos)