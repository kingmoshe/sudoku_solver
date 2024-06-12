from typing import Callable, List, Any, TypeVar
import time

T = TypeVar('T')


def calc_time(func: Callable[[Any], T], timer: List[float], *args, **kwargs) -> T:
    start_time = time.time()
    result = func(*args, **kwargs)
    timer[0] += time.time() - start_time
    return result
