"""
ou are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using
"""

import re


class Main():
    def __init__(self):
        self.n = int(input())

        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))


if __name__ == '__main__':
    obj = Main()