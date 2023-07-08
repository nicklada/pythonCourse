#!/usr/bin/env python3
import mymodule
from param import selectBiggest

print(mymodule.sayhi())
print(mymodule.__name__)
print(mymodule.__version__)
print(selectBiggest(2,5))

