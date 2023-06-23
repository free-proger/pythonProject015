#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# Кортежи. Конкатенация +
# Конкатенация двух кортежей
A = (1, 2, 3)
B = (4, 5, 6)
C = A + B # C = (1, 2, 3, 4, 5, 6)
# Конкатенация кортежей со сложными объектами
D = (3, "abc") + (-7.22, ['a', 5]) # D = (3, 'abc', -7.22, ['a', 5])
# Конкатенация трех кортежей
A = ('a', 'aa', 'aaa')
B = A + (1, 2) + (True, False) # B = ('a', 'aa', 'aaa', 1, 2, True, False)