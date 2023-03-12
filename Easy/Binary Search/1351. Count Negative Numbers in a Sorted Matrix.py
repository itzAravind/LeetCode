class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        positives = 0
        k = len(grid[0])

        for i in  grid:
            l,r=0,k

            while l<r:
                mid = (l+r)//2
                if i[mid]>=0:
                    l = mid + 1
                else:
                    r = mid 

            positives += l
            k = l

    // If all the number in the list are negative, stop searching
    // because this means that the following numbers are also negative.
            if r == 0:
                break

        return len(grid) * len(grid[0]) - positives