from forbiddenfruit import curse
from collections.abc import Iterable
from inspect import signature
from types import *

_func_types = [FunctionType, LambdaType, MethodType, BuiltinFunctionType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType]


def _pipe(self, func):
    if func == print:
        func(self() if callable(self) else self)
    else:
        def wrapper(*args, **kwargs):
            """Wrapper for the function combination"""
            res = self(*args, **kwargs) if callable(self) else self
            if len(signature(func).parameters) > 1:
                if isinstance(res, dict):
                    return func(**res)
                if isinstance(res, Iterable):
                    return func(*res)
            return func(res)

        return wrapper


for t in _func_types:
    curse(t, "__or__", _pipe)