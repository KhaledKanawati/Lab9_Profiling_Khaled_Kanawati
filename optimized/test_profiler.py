import time
import memory_profiler
import unittest
from profiler import slow_function, optimized_fast_function, memory_intensive_function


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    def test_slow_function(self):
        duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.2f} seconds.")
        self.assertGreater(duration, 2)

    def test_optimized_fast_function(self):
        duration = self.time_function(optimized_fast_function)
        print(f"optimized_fast_function executed in {duration:.2f} seconds.")
        self.assertLess(duration, 1)

    def test_memory_intensive_function(self):
        mem_usage_before = memory_profiler.memory_usage()
        duration = self.time_function(memory_intensive_function)
        mem_usage_after = memory_profiler.memory_usage()
        print(f"memory_intensive_function executed in {duration:.2f} seconds.")
        print(f"Memory before: {mem_usage_before[0]:.2f} MiB, after: {mem_usage_after[0]:.2f} MiB.")
        self.assertLess(duration, 5)
        # The loop does not have to increase memory usage.


def main():
    unittest.main()


if __name__ == "__main__":
    main()
