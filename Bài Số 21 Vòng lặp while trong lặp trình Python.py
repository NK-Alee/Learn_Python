# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:00:13 2024

@author: Alee
Bài số 21 Vòng lặp while trong lặp trình Python
"""
"""
Vòng lặp while trong Python là gì ?
Vòng lặp while trong Python được sử dụng để lặp một khối mã khi biểu thức kiểm tra (điều kiện) còn đúng.
Chúng ta thường sử dụng vòng lặp này khi chúng ta không biết trước số lần lặp lại
"""
# Yêu cầu người dùng nhập vào một con số n>0. nếu nhập sai thì yêu cầu người dùng nhập lại
"""n = -1

while (n<=0):
    n = int(input("Nhập vào n: "))

i = 0
tong = 0
while (i<=n):
    tong+=i # Tương đương tong = tong + i
    i+=1 # Tương đương i = i + 1
print("Tổng = ",tong)
"""
# Ví dụ với lệnh while else
"""j = 0
while (j<=10):
    print(j, "-Bên trong vòng lặp")
    j+=1
else:
    print(j, "Bên ngoài vòng lặp")
"""
# Ví dụ với lệnh while else và break để ngắt ngang vòng lặp
j = 0
while (j<=10):
    print(j, "-Bên trong vòng lặp")
    j+=1
    print("Tiếp tục thêm đơn vị")
    if(j>=6):
        print("Ngắt ngang vòng lặp")
        break
else:
    print(j, "Bên ngoài vòng lặp")