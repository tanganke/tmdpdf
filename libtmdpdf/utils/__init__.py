R"""
misc usefull functions and classes.
"""
from . import color_logging, print_h5, timeit
from .timeit import *
from .args import *


def first(iterable):
    return next(iter(iterable))
