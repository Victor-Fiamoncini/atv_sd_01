''' This module defines all app decorators '''

import time

from typing import Callable

def benchmark(function_to_track: Callable) -> Callable:
    ''' This decorator track the time taken to execute the input function '''

    def wrapped(*args, **kwargs):
        start = time.time()
        func_return = function_to_track(*args, **kwargs)
        end = time.time()-start

        print(f'Executing {function_to_track.__name__} function took {end} seconds')

        return func_return

    return wrapped
