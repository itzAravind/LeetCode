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

