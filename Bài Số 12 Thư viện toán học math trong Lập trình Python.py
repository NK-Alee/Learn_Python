# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:56:06 2024

@author: Alee
Bài Số 12. Thư viện toán học math trong Lập trình Python
"""
"""
Link Tham Khảo : https://docs.python.org/3/library/math.html 

1. Một số hàm quan trọng:

math.ceil(x)
Trả về giá trị trần của x , số nguyên nhỏ nhất lớn hơn hoặc bằng x

math.fabs(x)
Trả về giá trị tuyệt đối của x

math.floor(x)
Trả về sàn của x , số nguyên lớn nhất nhỏ hơn hoặc bằng x.

math.exp(x)
Trả về e lũy thừa x , trong đó e= 2,718281... là cơ số của logarit tự nhiên

math.log(x[,base])
Với một đối số, trả về logarit tự nhiên của x (cơ số e)

math.pow(x,y)
Trả về x lũy thừa y

2. Một số giá trị constants 

math.pi 
Hằng số toán hoạc pi = 3,141592....

math.e
Hằng số toán học e = 2,718281
"""
import math

x = float(input("x: "));

print("pi = ", math.pi)

print("|x|= ", math.fabs(x))

print("sqrt(x)= ", math.sqrt(x))

print("ceil(x)= ", math.ceil(x))

print("floor(x)= ", math.floor(x))