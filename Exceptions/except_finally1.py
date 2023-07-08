#!/usr/bin/env python3
import time
with open ('song.txt', 'r') as f:
    while True:
      line = f.readline()
      print(line)
      if len(line) == 0:
          break
      time.sleep(2)