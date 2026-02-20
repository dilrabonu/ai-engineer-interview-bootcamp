# Iterator  always using by __next__, __iter__ methods
class BatchIterator:
    """Custom iterator for mini-batch training data"""
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0  

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch

loader = BatchIterator(list(range(1, 11)), batch_size=3)
for batch in loader:
    print(batch)

