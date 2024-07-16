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

# Cách 2 phương thức .update

sinhvien.update({"malop" : "DH03" ,"diemtrungbinh" : 8.6})

print(sinhvien)

# Thêm cặp key value

# Cách 1

sinhvien["namhoc"] = 2025

print(sinhvien)

# Cách 2 .update

sinhvien.update({"noisinh" : "Dong Nai"})

print(sinhvien)

# Xóa đi loại bỏ các mục

"""
# Cách 1 phương thức pop() loại bỏ mục có tên khóa được chỉ định

sinhvien.pop("noisinh")

print(sinhvien)

# Cách 2 phương thức popitem() xóa mục được chèn cuối cùng (trong các phiên bản trước 3.7), thay vào đó , một mục ngẫu nhiên sẽ bị xóa :
    
sinhvien.popitem()

print(sinhvien)   

# Cách 3 phương thức del khóa loại bỏ mục có tên khóa được chỉ định , hoặc toàn bộ từ điển:

del sinhvien["hovaten"]

print(sinhvien)

# Cách 4 phương thức clear() xóa đi toàn bộ hàm thư viện

print(sinhvien)

sinhvien.clear()

print(sinhvien)
"""
# In tất cả các tên khóa trong từ điển , từng cái một:

for x in sinhvien:
    print(x)
    
# Duyệt các giá trị value
for x in sinhvien.values():
    print(x)
    
# Duyệt các khóa key 
for x in sinhvien.keys():
    print(x)
    
# Duyệt các cặp khóa - giá trị:
for x, y in sinhvien.items():
    print(x, y)
