class ProductOfNumbers:

    def __init__(self):
        self.size = 0
        self.zero = -1
        self.where, self.factor = [], []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero, self.where, self.factor = self.size, [], []
        elif num > 1:
            self.where.append(self.size)
            self.factor.append(num)
        
        self.size += 1

    def getProduct(self, k: int) -> int:
        start = self.size - k
        if self.zero >= start:
            return 0
        return prod(self.factor[bisect_left(self.where, start):])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)