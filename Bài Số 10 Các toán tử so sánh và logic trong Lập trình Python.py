# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:19:56 2024

@author: Alee
Bài số 10. Các toán tử so sánh và logic trong Lập trình Python
"""
"""
1.So Sánh
Toán Từ = Ý Nghĩa = Ví Dụ
> = Lớn Hơn = x > y

< = Nhỏ Hơn = x < y

== = Bằng = x == y

!= = Khác,Không Bằng = x != y

>= = Lớn Hơn hoặc Bằng = x >= y

<= = Nhỏ Hơn hoặc Bằng = x < y
"""
print("Ví dụ về so sánh:")
x = int(input("Nhập Số Thứ Nhất: "))
y = int(input("Nhập Số Thứ Hai: "))

#True hoặc False
print("{0}<{1} là {2}".format(x, y, x<y))
print("{0}>{1} là {2}".format(x, y, x>y))
print("{0}={1} là {2}".format(x, y, x==y))
print("{0}!={1} là {2}".format(x, y, x!=y))
print("{0}>={1} là {2}".format(x, y, x>=y))
print("{0}<={1} là {2}".format(x, y, x<=y))

"""
2.Logic
Toán Từ = Ý Nghĩa = Ví Dụ
and = Trả về giá trị True nếu tất cả các toán hạng là True = x and y

or = Trả về giá trị True nếu có ít nhất một toán hạng là True = x or y

not = Phủ định: True => False và False => True = not x
"""
print("Ví dụ về toán tử logic: ")
z = int(input("Nhập Số Thứ Ba: "))

print("{0}<{1} and {2}<{3} = {4}".format(x,y,y,z, (x<y) and (y<z)))

print("{0}<{1} or {2}<{3} = {4}".format(x,y,y,z, (x<y) or (y<z)))

print("not ({0}>{1}) = {2}".format(x,z,not (x>z)))