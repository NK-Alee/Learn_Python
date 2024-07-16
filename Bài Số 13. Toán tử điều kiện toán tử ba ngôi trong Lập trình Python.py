# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:29:43 2024

@author: Alee
Bài 13. Toán tử điều kiện | toán tử ba ngôi trong Lập trình Python
"""

"""
Cú Pháp
[tra về khi điều kiện đúng] if [điều kiện] else [trả về khi điều kiện sai ]
"""
#Ví dụ
#x = "ĐÚNG" if (5>3) else "SAI"

x = input ("Nhập vào số nguyên: ")
x = int (x)

kq = "Chẵn" if (x%2==0) else "Lẻ"

print (x, "Là số :", kq)