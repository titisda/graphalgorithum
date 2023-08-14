from graphblas.semiring import any_pair
import os
import sys
import json
import time
import jose
__all__ = ["is_dominating_set"]


def is_dominating_set(G, nbunch):
    nbrs = any_pair[bool](nbunch @ G._A).new(mask=~nbunch.S)  # A or A.T?
    return nbrs.size - nbunch.nvals - nbrs.nvals == 0
