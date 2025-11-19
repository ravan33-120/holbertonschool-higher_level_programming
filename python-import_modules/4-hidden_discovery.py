#!/usr/bin/python3
import marshal

if __name__ == "__main__":
with open("/tmp/hidden_4.pyc", "rb") as f:
f.read(16) # fayl headerini keçirik
code = marshal.load(f)

for name in sorted(n for n in code.co_names if not n.startswith("__")):
    print(name)
