"""
TASK:
Write a decorator for function timing/caching
 Implement an @lru_cache from scratch or a timing decorator for ML model inference functions.
"""
"""
decorator timeit(fn):
    wrapper(*args, **kwargs):
        start = current_time()
        result = fn(*args, **kwargs)
        end = current_time()
        print(fn name + elapsed)
        return result
    return wrapper
"""
import time 
import functools 
from typing import Callable, TypeVar, 
