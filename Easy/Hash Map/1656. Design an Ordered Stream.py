class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        res = []
        if self.ptr == idKey - 1:
            while self.ptr < len(self.arr) and self.arr[self.ptr] != "":
                print(self.ptr)
                res.append(self.arr[self.ptr])
                self.ptr += 1

        return res
    
    
 """The __init__ method initializes the data structure with a size n, which represents the total number of elements in the stream. It creates an empty array of length n and initializes a pointer ptr to 0.

The insert method takes two parameters: idKey, which represents the ID of the element being inserted, and value, which represents the value of the element being inserted. The method inserts the value into the array at the position idKey-1. Then, it checks if the ptr is at the same position as idKey-1. If it is, the method iterates through the array from ptr to the end of the array, appending each non-empty value to a list res. The ptr is then updated to the first empty position in the array.

Finally, the method returns the list res, which contains all the non-empty values that were inserted since the last call to insert with an ID greater than the current ID.

Note that the use of print(self.ptr) is unnecessary and may cause unexpected output when using the insert method. Also, the return statement should not include the res variable name, as it is not necessary."""
