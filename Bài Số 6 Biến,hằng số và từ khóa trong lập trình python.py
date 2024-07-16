# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:55:45 2024

@author: Alee
Bài Số 6: Biến, hằng số và từ khóa trong Lập trình Python
"""

"""Biến
Một biến là một vị trí được đặt tên, nó được sử dụng để lưu trữ dữ liệu trong bộ nhớ.
Giá trị của nó có thể được thay đổi khi thực chạy chương trình."""

# Ví dụ gán giá trị cho một biến
x = 5
print(x)

y = 15
y = 10
print(y)

# Ví dụ gán giá trị cho nhiều biến và có giá trị khác nhau
x, y, z = 1, 2, "Xin Chào"
print(x)
print(y)
print(z)

# Ví dụ gán giá trị cho nhiều biến và có giá trị giống nhau
x = y = z = "Alee"
print(x)
print(y)
print(z)

""" Hằng Số
Hằng số là một loại biến có giá trị không thể thay đổi
Trong Python không thực sự có hằng số
Hắng số thường được khai báo và gán trong một mô-đun và người dùng hạn chế không thay đổi giá trị
Của nó. Ở đây, mô-đun là một tệp mới chứa các biến, hàm, v.v được nhập vào tệp chính. Bên trong mô-đun,
các hằng số được viết bằng tất cả các chữ cái in hoa và dấu gạch dưới ngăn cách các từ."""

# Ví dụ:
PI = 3.14
print(PI)
PI = 3.1415
print(PI)

#Ví dụ:
import math
print(math.pi)

"""Cách đặt tên biến và hằng số
Chúng ta có thể sử dụng các chữ cái (a-z, A-Z),các con số(0-9), dấu gạch dưới_để đặt tên cho biến hoặc hằng số."""
#Ví Dụ:
content = "Học lập trình Python"

"""Tên biến có ý nghĩa và phù hợp với nội dung cần chứa."""
#Nên Sử Dụng
full_name = "LÊ HOÀNG ÂN"
#Thay vì:
x = "NGUYEN VAN A"

"""Nếu tên biến có nhiều từ hãy sử dụng dấu _ để ngăn cách, hoặc viết hoa các chữ cái của từng từ."""
#Ví dụ
ho_va_ten = "An Le"
fullName = "An Le"

"""Sử dụng các chữ cái viết hoa (toàn bộ) để khai báo các hằng số."""
#Ví Dụ:
PI = 3.14

#Không được bắt đầu bằng một chữ số (Chương trình sẽ gặp lỗi)

#Không sử dụng từ khóa làm tên biến hoặc hằng số