from forbiddenfruit import curse
from collections.abc import Iterable
from inspect import signature
from types import *

_func_types = [FunctionType, LambdaType, MethodType, BuiltinFunctionType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType]


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
curse(float, "abs", lambda self: abs(self))
curse(Iterable, "all", lambda self: abs(self))

print([True, True].all())
