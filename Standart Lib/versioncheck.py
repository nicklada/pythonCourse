#!/usr/bin/env python3
import sys
import warnings

if sys.version_info[0]<3:
    warnings.warn("Для выполнения этой программы необходима как минимум \ версия Python 3.0",
          RuntimeWarning)
else:
    print(sys.version_info)