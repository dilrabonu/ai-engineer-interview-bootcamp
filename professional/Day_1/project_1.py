"""
Question:
Implement a custom iterator / generator Build a data pipeline
 generator that reads large CSV files 
in chunks without loading everything into memory. 
"""
"""
Option A
function stream_csv(path, chunk_size)
open file
read header
create empty chun list
for each row in file:
    parse row
    add row to chunk
    if chunk has chunk_size rows:
        yield chunk
        reset chunk
    if chunk not empty:
        yield chunk
"""
# Implementation
from __future__ import annotations
import csv
from typing import Dict, Iterator, List, Optional


def read_csv_chunks(path: str, chunk_size: int =1000,  *, encoding: str ="utf-8", delimiter: str = ",",) -> Iterator[List[Dict[str, str]]]:
    """
    Stream large CSV file in chunks (list of rows, without loading everything into memory.
    
    Yields:
         A list of rows, where each row is a dcit: {column_name: value_as_string}

    Why Dict[str, str]?
        - Using csv.DictReader keeps columns explicit and safe
        - Values are strings by default; you can cast later in your pipeline.

    When:
        - Large CSVs (millions of rows)
        - ETL / feature extraction / batch ML inference
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    # Open file once, keep it open while streaming rows
    with open(path, mode="r", encoding=encoding, newline="") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        
        chunk: List[Dict[str, str]] = []
        for row in reader:
            chunk.append(row)

            if len(chunk) >= chunk_size:
                yield chunk
                chunk = [] # reset to free memory of previous chunk

               
        if chunk:
            yield chunk



# 2 implementation with custom iterator
from __future__ import annotations

import csv
from typing import Dict, List, Optional

class CSVChunkIterator:
    """
    Custom iterator that returns chunks of rows from CSV

    Why class iterator?
        - You may want expilict state, manual close(), reuse, or extra methods.
        - Shows you understand Python iterator protocol: __iter__ and __next__.
    """

    def __init__(self, path: str, chunk_size: int = 1000, *, encoding: str = "utf-8", delimiter: str = ",") -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be a positive integer")

        self.path = path
        self.chunk_size = chunk_size
        self.encoding = encoding
        self.delimiter = delimiter

        self._file = open(path, mode="r", encoding=encoding, newline="")
        self._reader = csv.DictReader(self._file, delimiter=delimiter)
        self._closed = False

    def __iter__(self) -> "CSVChunkIterator":
        # Iterator return itself
        return self

    def __next__(self) -> List[Dict[str, str]]:
        if self._closed:
            raise StopIteration

        chunk: List[Dict[str, str]] = []
        try:
            for _ in range(self.chunk_size):
                row = next(self._reader)
                chunk.append(row)
        except StopIteration:
            self.close()

        if not chunk:
            raise StopIteration

        return chunk
    def close(self) -> None:
        if not self._closed:
            self._file.close()
            self.closed = True

    def __enter__(self) -> "CSVChunkIterator":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

