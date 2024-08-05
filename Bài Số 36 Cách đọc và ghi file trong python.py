# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 01:03:44 2024

@author: Alee
Bài số 36 Cách đọc và ghi file trong python
"""
# Tạo và đọc file - open()

# "x" option - tạo file
try:
    f = open("vidu1.txt", "x")
except Exception as e:
    print(e)
finally:
        f.close()
# "w" - ghi dữ liệu vào file
try:
    with open ("vidu1.txt", "w") as f:
        f.write("Xin chào các bạn.")
        f.close()
except Exception as e:
    print(e)
    
# "a" - nối dữ liệu vào file
try:
    with open ("vidu1.txt", "a") as f:
        f.write("Xin chào các bạn.\n")
        f.close()
except Exception as e:
    print(e)
    
# "r" - đọc file
try:
    with open ("vidu1.txt", "r") as f:
        noidung = f.read()
        print(noidung)
except Exception as e:
    print(e)

# "r" - đọc file
try:
    with open ("vidu1.txt", "r") as f:
        noidung = f.readline()
        print(noidung)
except Exception as e:
    print(e)
    
# encoding = utf-8
f = open('vidu1.txt', encoding='utf-8')
f = open('vidu1.txt', mode='w', encoding='utf-8')
f = open('vidu1.txt', mode='a', encoding='utf-8')
f = open('vidu1.txt', mode='x', encoding='utf-8')
f = open('vidu1.txt', mode='r', encoding='utf-8')