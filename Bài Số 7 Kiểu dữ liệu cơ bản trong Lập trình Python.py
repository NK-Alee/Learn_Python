# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:48:05 2024

@author: Alee
Bài Số 07. Kiểu dữ liệu cơ bản trong Lập trình Python
"""
"""
1.Các kiểu dữ liệu cơ bản trong Python
Python là một ngôn ngữ thông dịch (Không yêu cầu biên dịch), được đặc trưng bởi hệ thống kiểu động - 
bạn không bắt buộc phải khao báo kiểu của biến .Trình thông dịch tự đoán kiểu dữ liệu
Kiểu Dữ Liệu
int ví dụ x = 1 = (số nguyên)
float ví dụ x = 1.0 = (số thực)
complex ví dụ x = 1 + 2j (số phức)
bool ví dụ x = True (Boolean: True/False)
str ví dụ x = 'abc' (String:Chuỗi ký tự)
Nonetype ví dụ x = none (Đối tượng đặc biệt chỉ ra null)

2. Ưu nhược điểm của kiểu dữ liệu động
Hệ thống kiểu dữ liệu động có cả hai ưu điểm:
    *Viết mã nhanh hơn
    *Ít mã hơn
Và nhược điểm:
    *Thời gian chạy lâu hơn
    *khả năng xảy ra lỗi khó gỡ lỗi
Python cho phép thay đổi kiểu dữ liệu của biến

3. Cách kiểm tra dữ liệu của biến
Sử dụng câu lệnh: type(tên_biến)"""
# Ví dụ 
e = 2.72
PI = "3.14"
text = "Hello World"

print("Kiểu dữ liệu của biến e : ", type(e),
      "Kiểu dữ liệu của biến PI : ", type(PI),
      "Kiểu dữ liệu của biến text : ", type(text))

# Code thực tế
x = 1
print (type(x))
x = 1.0
print (type(x))
x = 1 + 2j
print (type(x))
x = True
print (type(x))
x = 'abc'
print (type(x))
x = None
print (type(x))

"""
4. Lưu ý và cẩn trọng khi tianh1 toán giữa các kiểu dữ liệu"""