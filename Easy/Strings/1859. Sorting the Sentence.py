class Solution:
    def sortSentence(self, s: str) -> str:
        str1 = s[::-1].split()
        str1.sort()
        result = []
        for i in str1:
            result.append(i[1:][::-1])
        return " ".join(result)

"""The given solution is a simple and efficient approach to sorting a sentence based on the index of each word. The time complexity of the solution is dominated by the sorting step, which takes O(N log N) time in the worst case, where N is the number of words in the sentence.

The initial step of reversing the input string and splitting it into words takes O(N) time, where N is the length of the input string. However, this step is negligible compared to the sorting step, which dominates the time complexity of the algorithm.

The final step of joining the sorted words together also takes O(N) time, where N is the number of words in the sentence. However, this step is also negligible compared to the sorting step.

Overall, the time complexity of the solution is optimal for the given problem, as it is not possible to sort a list of words in less than O(N log N) time in the worst case. Therefore, the given solution is a good approach for sorting a sentence based on the index of each word."""
