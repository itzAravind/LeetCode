class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=zip(heights,names)
        l=[]
        for i,j in sorted(a):
            l.append(j)
        return l[::-1]
    
"""This code defines a Solution class that contains a sortPeople method. The method takes in two parameters: names, a list of strings representing people's names, and heights, a list of integers representing their heights.

The method first uses the zip function to create a list of tuples, where each tuple contains a person's height and their corresponding name. It then sorts the list of tuples in ascending order based on the heights of the people.

The method finally creates an empty list and iterates through the sorted list of tuples in ascending order, appending each person's name to the list. The resulting list is then reversed and returned in descending order based on height.

Overall, this code provides a simple and efficient solution to sorting a list of people's names based on their heights in descending order."""
