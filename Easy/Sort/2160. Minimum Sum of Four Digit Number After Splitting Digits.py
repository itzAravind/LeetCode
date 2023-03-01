class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        return int(num[0]+num[-1])+int(num[1]+num[2])
  
"""This is a Python class named Solution that has a method minimumSum. This method takes an integer num as input and returns an integer.

The method first converts the input integer to a list of its digits by using the str function to convert the integer to a string, and then using the list function to convert the string to a list of its characters (which are the digits of the original integer).

Next, it sorts the list of digits in ascending order using the sort method.

Finally, the method concatenates the smallest and largest digits of the sorted list using the + operator and converts the resulting string to an integer using the int function. It does the same for the second smallest and second largest digits. It then returns the sum of these two integers, which is the minimum possible sum that can be obtained by adding two two-digit numbers that can be formed using the digits of the original integer."""
