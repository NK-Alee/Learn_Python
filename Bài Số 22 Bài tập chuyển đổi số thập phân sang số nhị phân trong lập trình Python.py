# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:43:05 2024

@author: Alee
Bài Số 22 Bài tập chuyển đổi số thập phân sang số nhị phân trong lập trình Python
"""
# Nhập n (n>0)
n = -1
while (n<=0):
    n = int(input("Nhập vào n>0 : "))

# Chuyển từ thập phân sang nhị phân
ketqua = ""
while(n>0):
    ketqua = str(n%2)+ketqua
    print("n%2 = ", n%2)
    n = n//2
    print("n = ", n)

print("Kết quả:", ketqua)