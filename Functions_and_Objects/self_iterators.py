class CustomRange:
	def __init__(self, max):
		self.max = max

	def __iter__(self):
		self.curr = 0
		return self

	def next(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb


for i in CustomRange(10):
    print
    i

    # output:
    # 0 1 2 3 4 5 6 7 8 9
