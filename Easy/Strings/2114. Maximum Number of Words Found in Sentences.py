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



