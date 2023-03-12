class Solution:
    def answerQueries(self, A: list[int], Q: list[int]) -> list[int]:
        A.sort()
        A = list(accumulate(A))
        return [bisect_right(A, q) for q in Q]  # bisect_right(A, e) returns largest i s.t., for x in A[i:], e < x