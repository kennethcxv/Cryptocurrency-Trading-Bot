import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.calls = []
        self.max_calls = max_calls
        self.period = period

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            current_time = time.time()
            self.calls = [call for call in self.calls if call > current_time - self.period]
            if len(self.calls) < self.max_calls:
                self.calls.append(current_time)
                return func(*args, **kwargs)
            else:
                time_to_wait = self.period - (current_time - self.calls[0])
                time.sleep(time_to_wait)
                return wrapped_func(*args, **kwargs)
        return wrapped_func
