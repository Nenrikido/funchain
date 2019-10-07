# pipeoperatory.py
Adding a pipe-line function execution operator to python

- Example usages : 
```py
import pipeoperator

def double(x):
    return 2 * x

2 | double | double | double | print # 16

map(str.lower | str.capitalize, ["mEsSy", "tExT"]) | print # Messy Text
```
