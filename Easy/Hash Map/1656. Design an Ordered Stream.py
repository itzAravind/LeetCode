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