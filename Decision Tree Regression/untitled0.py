# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:54:29 2017

@author: ARSHABH SEMWAL
"""

import textwrap
def merge_the_tools(string, k):
    y=textwrap.wrap(string,k)
    print(y)
    for i in range(int(len(string)/k)):
        print(''.join(set(y[i])))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
        