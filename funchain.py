from forbiddenfruit import curse
from collections.abc import Iterable
from inspect import signature
from types import *
import sys

_func_types = [FunctionType, LambdaType, MethodType, BuiltinFunctionType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType]
_numbers = [int, float, complex]
_iterables = [list, tuple, range, str, dict, bytes, bytearray, memoryview, set, frozenset]


def _pipe(self, func):
    def wrapper(*args, **kwargs):
        """Wrapper for the function combination"""
        res = self(*args, **kwargs) if callable(self) else self
        try:
            if func == print or len(signature(func).parameters) > 1:
                if isinstance(res, dict):
                    return func(**res)
                if isinstance(res, Iterable):
                    return func(*res)
        except:
            pass
        return func(res)

    if func == print:
        wrapper()
    else:
        return wrapper


for t in _func_types:
    curse(t, "__or__", _pipe)

for i in _iterables:
    curse(i, "all", lambda self: all(self))
    curse(i, "any", lambda self: any(self))
    curse(i, "dict", lambda self, **kwargs: dict(self, **kwargs))
    curse(i, "enumerate", lambda self, start=0: enumerate(self, start))
    curse(i, "filter", lambda self, function: filter(self, function))
    curse(i, "len", lambda self: len(self))
    curse(i, "list", lambda self: list(self))
    curse(i, "map", lambda self, function: map(self, function))
    curse(i, "max", lambda self, key=None, default=None: max(self, key, default))
    curse(i, "min", lambda self, key=None, default=None: min(self, key, default))
    curse(i, "reversed", lambda self: reversed(self))
    curse(i, "set", lambda self: set(self))
    curse(i, "sorted", lambda self, key=None, reverse=False: sorted(self, key=key, reverse=reverse))
    curse(i, "sum", lambda self, start=None: sum(self, start))
    curse(i, "tuple", lambda self: tuple(self))
    curse(i, "zip", lambda self, *iterables: zip(self, *iterables))

for n in _numbers:
    curse(n, "abs", lambda self: abs(self))
    curse(n, "pow", lambda self, y, z=None: pow(self, y, z))
    curse(n, "round", lambda self, ndigits=None: round(self, ndigits))

curse(bytes, "open",
      lambda self, file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: open(self, mode, buffering, encoding,
                                                                                                                           errors, newline, closefd))

curse(int, "bin", lambda self: bin(self))
curse(int, "chr", lambda self: chr(self))
curse(int, "divmod", lambda self, b: divmod(self, b))
curse(int, "hex", lambda self: hex(self))
curse(int, "oct", lambda self: oct(self))
curse(int, "range", lambda self, stop=None, step=None: range(self, stop, step))

curse(float, "divmod", lambda self, b: divmod(self, b))

curse(str, "eval", lambda self, globals=None, locals=None: eval(self, globals, locals))
curse(str, "open",
      lambda self, file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: open(self, mode, buffering, encoding,
                                                                                                                           errors, newline, closefd))
curse(str, "ord", lambda self: ord(self))

curse(type, "super", lambda self, arg=None: super(self, arg))

curse(object, "ascii", lambda self: ascii(self))
curse(object, "bool", lambda self: bool(self))
curse(object, "bytearray", lambda self, encoding=None, error=None: bytearray(self, encoding, error))
curse(object, "bytes", lambda self, encoding=None, error=None: bytes(self, encoding, error))
curse(object, "callable", lambda self: callable(self))
curse(object, "complex", lambda self, imag=None: complex(self, imag))
curse(object, "delattr", lambda self, name: delattr(self, name))
curse(object, "dir", lambda self, name: dir(self, name))
curse(object, "exec", lambda self, globals=None, locals=None: exec(self, globals, locals))
curse(object, "float", lambda self: float(self))
curse(object, "format", lambda self, format_spec=None: format(self, format_spec))
curse(object, "frozenset", lambda self: frozenset(self))
curse(object, "getattr", lambda self, name, default=None: getattr(self, name, default))
curse(object, "hasattr", lambda self, name: hasattr(self, name))
curse(object, "hash", lambda self: hash(self))
curse(object, "help", lambda self: help(self))
curse(object, "id", lambda self: id(self))
curse(object, "input", lambda self: input(self))
curse(object, "int", lambda self, base=10: int(self, base))
curse(object, "isinstance", lambda self, classinfo: isinstance(self, classinfo))
curse(object, "issubclass", lambda self, classinfo: issubclass(self, classinfo))
curse(object, "iter", lambda self, sentinel=None: iter(self, sentinel))
curse(object, "max", lambda self, arg2, *args, key=None: max(self, arg2, *args, key))
curse(object, "memoryview", lambda self: memoryview(self))
curse(object, "min", lambda self, arg2, *args, key=None: min(self, arg2, *args, key))
curse(object, "print", lambda self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False: print(self, *objects, sep, end, file, flush))
curse(object, "repr", lambda self: repr(self))
curse(object, "setattr", lambda self, name, value: setattr(self, name, value))
curse(object, "slice", lambda self, stop=None, step=None: slice(self, stop, step))
curse(object, "str", lambda self, encoding='utf-8', errors='strict': str(self, encoding, errors))
curse(object, "type", lambda self, bases=None, dict=None: type(self, bases, dict))
curse(object, "vars", lambda self: vars(self))
