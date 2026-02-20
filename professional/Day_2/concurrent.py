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
from multiprocessing import Pool
import os 

def train_fold(fold_id):
    """ 
    Train model on one CV fold - CPU-intensive.
    """
    print(f"Fold {fold_id} on PID {os.getpid()}")
    return {"fold": fold_id, "accuracy": 0.90 + fold_id * 0.01}

with Pool(processes=4) as pool:
    results = pool.map(train_fold, range(5))
    for r in results:
        print(f"Fold {r['fold']}: acc={r['accuracy']}")

# Asyncio

import asyncio 

async def fetch_api(session, url):
    """ Async HTTP request - non-blocking I/O"""
    await asyncio.sleep(0.1)
    return {"url": url, "status": 200}

async def fetch_all():
    """Fetch multiple API's concurrently"""
    urls = ["api/train", "api/val", "api/test"]
    tasks = [fetch_api(None, url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
results = asyncio.run(fetch_all())
print(results)