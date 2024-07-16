# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:41:43 2024

@author: Alee
Bài 18 Giới thiệu vòng lặp for trong lập trình Python
"""
# Vòng lặp => FOR

# Vòng lặp từ 0 đến < (n) Mỗi lần tăng một đơn vị
n = 11
for i in range (n):
    print(i)

# Ví dụ tính tổng từ 0 -> n
n =int (input("Nhập vào N : "))
tong = 0 
for i in range(n+1):
    tong+=i
print("tong = ", tong)

# Ví dụ vòng lặp for, có bước tăng tùy chỉnh 
for i in range(0, 10, 2): #< 0 là vị trí bắt đầu , 10 là vị trí đích , bước tăng
    print(i)

# Ví dụ vòng lặp for , bước giảm tùy chỉnh 
for i in range(10, 0, -1): #< 0 là vị trí bắt đầu , 10 là vị trí đích , bước tăng
    print(i)

# Ví dụ vòng lặp for duyệt các phần tử của biến    
colors = ["red", "green", "orange"]
for color in colors:
    print(color)

#Ví dụ vòng lặp for duyệt phần tử theo vị trí
for i in range (len(colors)):
    print(colors[i])