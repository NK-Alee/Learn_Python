# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 23:08:33 2024

@author: Alee
Bài Số 9 Các phép toán số học cơ bản trong Lập trình Python
"""
"""
PHÉP TOÁN 
(PHÉP TOÁN = GIẢI THÍCH = VÍ DỤ)
+ = CỘNG = x + y
- = TRỪ = x - y
* = NHÂN = x * y
/ = CHIA = x / y
% = CHIA LẤY DƯ = x % y
** = MŨ = x ** y
// = CHIA LẤY PHẦN NGUYÊN = x // y
"""

# Ví Dụ
a = input("NHẬP VÀO SỐ A: ")
print("Kiểu dữ liệu của A: ", type(a))
a = int(a)
print("Kiểu dữ liệu của A: ", type(a))
b = input("NHẬP VÀO SỐ B: ")
print("Kiểu dữ liệu của A: ", type(b))
b = int(b)
print("Kiểu dữ liệu của A: ", type(b))
print("{0}+{1}={2}".format(a, b, a+b))
print("{0}-{1}={2}".format(a, b, a-b))
print("{0}*{1}={2}".format(a, b, a*b))
print("{0}/{1}={2}".format(a, b, a/b))
print("{0}%{1}={2}".format(a, b, a%b))
print("{0}**{1}={2}".format(a, b, a**b))
print("{0}//{1}={2}".format(a, b, a//b))