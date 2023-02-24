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
    
 """This is a solution to the "Jewels and Stones" problem. The problem provides two strings jewels and stones. The jewels string represents the types of jewels that you have, and the stones string represents the stones that you have. Each character in stones represents a type of stone, and you want to know how many of the stones you have are also jewels.

The provided solution uses a dictionary map to keep track of the types of jewels. In the first loop, the solution iterates through each character in the jewels string and adds it to the dictionary with a value of 1. The value is not important in this case because we only care about the keys (which represent the types of jewels).

In the second loop, the solution iterates through each character in the stones string and checks if it exists in the dictionary map. If the character exists in the dictionary, it means that it is a jewel, so the result variable is incremented by 1.

Finally, the method returns the value of result, which represents the number of stones that are also jewels.

For example, if jewels is "abc" and stones is "acdddefff", the method will return 4 because there are 4 stones (2 as and 2 cs) that are also jewels. """
