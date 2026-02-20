# 3 Concurency
# Threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch_data(url, delay=0.5):
    time.sleep(delay)
    return {"url": url, "data": f"Data from {url}"}

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_data, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        result = future.result()
        print(f"Got {url}: {result}")

# MultiProcessing