# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:24:46 2024

@author: Alee
Bài số 30 Lambda Function trong Python
"""
"""
Python Lambda
Một hàm lambda là một hàm ẩn danh nhỏ.

Một hàm lambda có thể nhận bất kỳ số lượng đối số nào , nhưng chỉ có thể có một biểu thức

# Cú Pháp
lambda arguments : expression

"""
# Ví dụ 1

kiemtrasochan = lambda a : (a%2==0)
print(kiemtrasochan(5))
print(kiemtrasochan(4))

# Ví dụ 2
tinhtong = lambda a, b : a+b
print(tinhtong(5, 10))
print(tinhtong(-5, 2))

# Ví dụ về sử dụng lambda function bên trong các function
def hammuhai(a):
    return a**2

def hammuba(a):
    return a**3


###

def hammu(n):
    return lambda x : x**n

hammu2 = hammu(2)
hammu3 = hammu(3)
hammu4 = hammu(4)

print(hammu2(2))
print(hammu3(3))
print(hammu3(4))