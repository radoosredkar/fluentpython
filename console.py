import os

with open("FluentPython/console_ch14.py") as fp:
    src = fp.read(60)
print(len(src), src)
print(fp.closed, fp.encoding)

print("*" * 100)
