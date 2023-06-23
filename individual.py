#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # Проверить количество элементов кортежа.
    B = tuple(sorted(A))
    if A == B:
        print('Элементы в правильном порядке!')
    else:
        print('Элементы не в правильном порядке!')
