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

# Generator lazy method and helps to reduce memory usage and used with YIELD

def lazy_csv_reader(path, chunk_size=1000):
    """Read CSV lazily only chunk size rows in memory at once
    This handles 1000 GB++ files on a laptop with 8 GB RAM!"""
    import csv
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def lazy_csv_reader(path, batch_size=1000):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= batch_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

class BatchIterator:
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
def lazy_csv_reader(path, chunk_size=1000):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


