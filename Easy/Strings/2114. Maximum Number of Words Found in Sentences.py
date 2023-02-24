class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
#BrutFroce
#        word_count = []
#        for i in range(len(sentences)):
#           count = 1
#            for j in sentences[i]:
#               if j == " ":
#                    count += 1
#                word_count.append(count)
#            word_count.sort()
#        return word_count[-1]

# Replacing second for loop using count()
        word_count = []
        for i in sentences:
            word_count.append(i.count(" ")+1)
        word_count.sort()
        return word_count[-1]



"""This is a solution to the "Most Words Found in a Sentence" problem. The problem provides a list sentences of strings representing sentences. The problem asks to find the sentence that has the most number of words and return the count of words in that sentence.

The provided solution has two implementations. The first implementation (commented out) uses a nested loop to count the number of words in each sentence and add the count to a list word_count. After counting the words in all the sentences, the list is sorted in ascending order, and the last element (which corresponds to the maximum word count) is returned.

The second implementation (uncommented) replaces the nested loop with the count() method of the string object. The method counts the number of occurrences of the space character " " in each sentence and adds 1 to the count to get the total number of words. The counts are added to the word_count list, which is then sorted, and the last element (which corresponds to the maximum word count) is returned.

The second implementation is more concise and arguably easier to read than the first implementation. It also avoids the nested loop, which makes it more efficient for large inputs.

For example, if the input sentences is ["Hello world", "The quick brown fox jumps over the lazy dog"], the method will return 7, which is the word count in the second sentence. """
