class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        result =[]
        for i in range(len(indices)):
            if indices[i] not in dict:
                dict[indices[i]] = s[i]
        indices.sort()
        for j in indices:
            result.append(dict[j])
        return "".join(result)

"""This is a Python solution for the problem of restoring a string based on a given list of indices.

The solution defines a class called Solution with a single method called restoreString. The method takes in two arguments: a string s and a list of integers called indices. The goal of the method is to create a new string based on s, where the characters are arranged based on their corresponding indices in the indices list.

The solution uses a dictionary to keep track of the mapping between indices and characters in the original string s. It then sorts the indices list and uses it to construct the new string by appending the corresponding characters from the dictionary to a result list. Finally, the method returns the result list as a string using the join method.

Overall, the solution has a time complexity of O(nlogn), where n is the length of the indices list due to the sorting operation. However, the space complexity is O(n) since the solution uses a dictionary to store the character-index mappings."""
