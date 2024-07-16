# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:31:27 2024

@author: Alee
Bài số 27 Kiểu dữ liệu Dictionary
"""
"""
Dictionary ( Từ Điển )
Từ điền được sử dụng để lưu trữ các giá trị dữ liệu các cặp key : value.

Từ điển là một tập hợp được sắp xếp theo thứ tự *, có thể thay đổi và không cho phép trùng lặp.

Kể từ phiên bản Python 3.7 , các từ điển được sắp xếp theo thứ tự

Từ điển được viết bằng dấu ngoặc nhọn { } và có các khóa và giá trị

Từ điển có thể thay đổi, nghĩa là chúng ta có thể thay đổi, thêm hoặc bớt các mục sau khi từ điển đã được tạo

Từ điển không thể có hai mục với cùng một khóa

"""
# Ví dụ
sinhvien = {
"hovaten": "Nguyen Van A",    
"malop": "DH01",
"diemtrungbinh": 8.5
}
print(sinhvien)

print(sinhvien["hovaten"])

# Su dung get() để lấy giá trị
print(sinhvien.get("malop"))

# Cập nhật giá trị

# Cách 1

sinhvien["malop"] = "DH02"

print(sinhvien)

# Cách 2

sinhvien.update({"malop" : "DH03" ,"diemtrungbinh" : 8.6})

print(sinhvien)

# Thêm cặp key value

# Cách 1

sinhvien["namhoc"] = 2025

print(sinhvien)

# Cách 2

sinhvien.update({"noisinh" : "Dong Nai"})

print(sinhvien)