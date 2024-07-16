# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:28:29 2024

@author: Alee
Bài 14. Câu lệnh rẻ nhánh if else trong Lập trình Python
"""
"""
Câu lệnh if .. else là câu lệnh ra quyết định thực hiện một đoạn mã khi điều kiện đúng hoặc sai.

Dạng 1
if (điều kiện):
    các câu lệnh
"""
# Ví Dụ 1
x = input("Nhập số nguyên x : ")
x = int(x)

if x>0:
    print(x, "là số dương")

"""
Dạng 2 
if (điều kiện)
    các câu lệnh 1
else:
    các câu lệnh 2
"""
# Ví dụ 2

if x%2==0:
    print(x, "Là số chẵn")
else:
    print(x, "là số lẻ")

print("Kết thúc chương trình")

"""
Dạng 3
if (điều kiện 1)
    Các câu lệnh 1
elif (điều kiện 2)
    Các câu lệnh 2
else:
    Các câu lệnh 3
"""
#Ví dụ 3
if x>=9:
    print("Xếp loại: Xuất sắc")
elif x>=8:
    print("Xếp loại: Giỏi")
elif x>=7:
    print("Xếp loại: Khá")
elif x>=5:
    print("Xếp loại: Trung Bình")
else:
    print("Xếp loại: Yếu")
