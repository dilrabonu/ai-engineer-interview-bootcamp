"""
Question:
Implement a custom iterator / generator Build a data pipeline
 generator that reads large CSV files 
in chunks without loading everything into memory. 
"""
"""
open file at file_path
read header row automatically
Initialize empty chunk list

for each row in file;
add row to chunk list
if chunk list size == chunk_size:
    Yield chunk list
    reset chunk list to empty

if chunk list is not empty
Yield remaining rows

Close file
"""

import csv
from typing import Generator, List, Dict

def basic_csv_chunk_generator(
    file_path: str,
    chunk_size: int = 1000
) -> Generator[List[Dict], None, None]:
    with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        chunk: List[Dict] = []
        for row in reader:
            chunk.append(dict(row))
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
