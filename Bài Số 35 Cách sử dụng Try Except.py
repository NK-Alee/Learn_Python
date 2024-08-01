# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:48:23 2024

@author: Alee
Bài 35 Cách sử dụng Try Except
"""
"""
try:
    # Đoạnn code dự đoán có lỗi
except:
    # Hành động khi lỗi xảy ra
else:
    # Thực thi đoạn này nếu như mã không có lỗi
finally:
    # Cho phép bạn thực thi mã, bất kể kết quả cuac1 các khối try có bị lỗi hay không
"""
try:
    a = int(input("Nhập vào số nguyên a: "))
    print(str(a) + " + 5 =" +str(a+5))
    # Đoạn code dự đoán có lỗi
except Exception as e:
    print(e)
    # Hành động khi lỗi xảy ra
else:
    print("Không có lỗi xảy ra")
    # Thực thi đoạn này nếu như mã không có lỗi
#finally:
    print("Kết thúc chương trình!")
    # Cho phép bạn thực thi mã, bất kể kết quả cuac1 các khối try có bị lỗi hay không