# -*- coding: utf-8 -*-

"""
Created on Tue Jun 25 23:29:19 2024

@author: Alee
Bài 15 Bài tập giải phương trình bậc 2 trong Lập trình Python
"""

# import thư viện
import math
# Nhập dữ liệu
print("Giải phương trình ax^2+bx+c=0")
a =float(input("Nhập A: "))
b =float(input("Nhập B: "))
c =float(input("Nhập C: "))

print("{0}x^2+{1}x+{2}=0".format(a,b,c))

if(a!=0):
    delta = b**2 - 4*a*c 
    if (delta<0):
        print("Phương trình vô nghiệm")
    elif (delta==0):
        x = -b/(2*a)
        print("Có nghiệm kép x1=x2=", x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("Có nghiệm kép x1={0} x2={1}".format(x1, x2))
else:
    print("Không phải phương trình bậc 2")