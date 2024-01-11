import ast
import sys

import numpy as np
import pandas as pd


def replaceFunc(x: str) -> str:
    if x == "[null]":
        return "[]"
    elif x == "[null,null]":
        return "[]"
    elif "null," in x:
        return x.replace("null,", "")
    elif ",null" in x:
        return x.replace(",null", "")
    else:
        return x
