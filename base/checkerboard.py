# coding=utf-8
#!/usr/bin/python

#题目：要求输出国际象棋棋�?
#文件名：checkerboard.py
#  Jack Cui 2016.3.30
import sys
for i in range(8):
        for j in range(8):
                if (i + j) % 2 != 0:
                        print(chr(219),end = '')
                        print(chr(219),end = '')
                else:
                        print('  ',end = '')
        print('\n',end = '')