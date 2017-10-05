# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:46:28 2017

@author: ARSHABH SEMWAL
"""
if __name__ == '__main__':
    n = int(input())
    
if n % 2 == 0:
    
    if n >=2 and n<=5:
        print('Not Wierd')
        
    if n >=6 and n<=20:
        print('Wierd')

    if n >=20:
        print('Not Wierd')

else:
    print('Wierd')