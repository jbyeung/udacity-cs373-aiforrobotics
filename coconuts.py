#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jeffrey
#
# Created:     29/02/2012
# Copyright:   (c) Jeffrey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def solve(c):
    i = 0
    while i < 6:
        if not(c % 5 == 0) and ((c-1) % 5 == 0):
            c = 4 * (c - 1) / 5
        else:
            break
        i = i + 1
    return (i == 6)

x = 0
while True:
    if solve(x):
        break
    x = x + 1

print x