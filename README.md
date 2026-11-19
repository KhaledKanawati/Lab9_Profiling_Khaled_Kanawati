# Lab 9 Profiling in Python
Khaled Kanawati

I compared the original and optimized scripts using cProfile, line_profiler, memory_profiler, and coverage.py.

## Files
- `original/`: original scripts, tests, and HTML coverage report.
- `optimized/`: optimized scripts, tests, and HTML coverage report.
- `screenshots/`: terminal screenshots before and after optimization.
- `lab9_Khaled_Kanawati.docx`: results, screenshots, and analysis.

## Running the lab
Install the packages:
```bash
python -m pip install line_profiler memory_profiler coverage
```

Run these commands inside either `original` or `optimized`:
```bash
python -m cProfile -s time profiler.py
python profiler_lineprofiler.py
python -m memory_profiler profiler_memoryprofiler.py
python -m coverage run -m unittest discover
python -m coverage report -m
python -m coverage html
```

Open `htmlcov/index.html` to view coverage.

Both versions passed all three tests. The memory test records usage before and after without requiring an increase, as explained in the report.
