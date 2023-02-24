class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for i in operations:
            if "+" in i:
                result += 1
            else:
                result -= 1
        return result

"""This is a solution to the "Final Value of Variable After Performing Operations" problem. The problem provides a list operations of strings that represent operations to be performed on a variable x. The operations can be of two types:

"++X" or "X++" which increments the value of x by 1.
"--X" or "X--" which decrements the value of x by 1.
The problem asks to return the final value of x after performing all the operations.

The provided solution iterates through the list of operations and updates the value of result based on the type of operation. If the operation contains a "+" character, result is incremented by 1, and if the operation contains a "-" character, result is decremented by 1. Finally, the value of result is returned as the final value of x.

For example, if the input operations is ["--X", "X++", "X++"], the method will return 1. The first operation decrements x by 1, resulting in x = -1. The second operation then increments x by 1, resulting in x = 0. The third operation again increments x by 1, resulting in x = 1. So the final value of x is 1. """
