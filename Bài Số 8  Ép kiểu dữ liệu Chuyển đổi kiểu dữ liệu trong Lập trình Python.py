# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:48:33 2024

@author: Alee
Bài Số 8 Ép kiểu dữ liệu | Chuyển đổi kiểu dữ liệu trong Lập trình Python     

"""
"""
Ép kiểu hay còn gọi là chuyển đổi kiểu dữ liệu
Quá trình chuyển đổi giá trị của một kiểu dữ liệu (Số nguyên,chuỗi,số float,v.v) sang kiểu dữ liệu
khác được gọi là ép kiểu (chuyển đổi kiểu). Python có hai kiểu chuyển đổi kiểu

Chuyển đổi kiểu ngầm định: Python tự động chuyển đội một kiểu dữ liệu này sang kiểu dữ liệu khác.
Quá trình này không cần bất kỳ sự tham gia nào của người dùng"""
#Ví dụ
a = 5
b = 2.0
c = a/b
print("Kiểu dữ liệu của a: ", type(a))
print("Kiểu dữ liệu của b: ", type(b))
print("Kiểu dữ liệu của c: ", type(c))
"""
Chúng ta có thể thấy c có kiểu dữ liệu float vì Python luôn chuyển đổi kiểu dữ liệu nhỏ hơn sang kiểu
dữ liệu lớn hơn để tránh mất dữ liệu """

#Hãy thử đoạn code sau đây xem có gặp lỗi không?
"""
n = 100
m = "200"
print(n+m)
"""
"""Như trên có thể thấy đoạn code trên bị báo lỗi unsupported operand type(s) for +: 'int' and 'str' vì dữ liệu số thực không thể + với dữ liệu chuỗi
 
Chuyển đổi kiểu rõ ràng: do chúng ta thực gõ lệnh chuyển đổi kiểu dữ liệu của một đối tượng thành kiểu dữ liệu bắt buộc.
Chúng ta sử dụng các hàm có sẵn int(),float(),str(),v.v để thực hiện chuyển đổi
Cú pháp: ten_kieu_du_lieu(biến)
"""
#Ví dụ
n = 100
m = "200"
#ép kiểu n sang số thực
print(str(n)+m)
#ép kiểu m sang số nguyên
print(n+int(m))
