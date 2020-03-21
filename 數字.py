# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:15:54 2020

@author: TAITRA
"""
import random
counter = 0
answer = int(input())
while True:
    a = int(input("請猜數字1~100:"))  
    if answer == a:
        print("對了")
        break
    else:
        print("錯了")
        counter = counter+1
        if counter > 4:
            break