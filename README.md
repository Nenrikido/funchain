# funchain
Adding functions and methods chaining facilities to Python :

### Pipe operator :
```py
import pipeoperator

def double(x):
    return 2 * x

2 | double | double | double | print # 16

map(str.lower | str.capitalize, ["mEsSy", "tExT"]) | print # Messy Text
```

### Builtin functions as standard object methods :
```py
# function                  # equivalent
map(lambda x: x*2, [2, 3])  # [2, 3].map(lambda x: x*2)
chr(64)                     # 64.chr()
# ...
# Basically all builtin functions are available as methods now
```

## Requirements :
[forbiddenfruit](https://github.com/clarete/forbiddenfruit)

You can install it using :

`pip install forbiddenfruit`

(Please note that, as stated in their documentation, it is tested to work until version 3.3, but I developped this on version 3.7 where it works well, if you have some issues please report them to me and i will add informations here, also I didn't test it on other implementation than CPython, where it may or may not work, again, please report problems.)
