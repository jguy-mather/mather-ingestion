import sys

if sys.prefix == sys.base_prefix:
    exit(f"not in venv ==> {sys.prefix} equals {sys.base_prefix}")
else:
    pass