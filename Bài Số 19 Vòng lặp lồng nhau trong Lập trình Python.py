# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:45:08 2024

@author: Alee
Bài số 19 Vòng lặp lồng nhau trong Lập trình Python
"""
#Bài tập: In bảng cửu chương
for j in range (2, 10):
    print("Bảng cửu chương", j)
    for i in range (1,11):
        print("{0} x {1} = {2} ".format(j, i, j*i))
