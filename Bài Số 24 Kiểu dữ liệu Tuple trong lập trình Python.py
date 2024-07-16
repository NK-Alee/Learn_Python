# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:34:26 2024

@author: Alee
Bài số 24 Kiểu dữ liệu Tuple trong lập trình Python
"""
"""
1.Giới thiệu về Tuple
Tuple là một chuỗi các phần tử có thứ tự giống như một List. Sự khác biệt duy nhất là bộ giá trị các hằng số
Tuple một khi được tạo ra thì giá trị của nó không thể sửa đổi

Tuple được sử dụng để bảo vệ dữ liệu và thường nhanh hơn dữ liệu list vì chứng không thể thay đổi động.

Được định nghĩa trong dấu ngoặc đơn (), các mục được phân tách bằng dấu phẩy -,- .

Giá trị của Tuple có thể bị trùng lặp.
"""
#2. Ví dụ dữ liệu Tuple

gioitinh = ("Nam", "Nữ", "lGBT")

lophoc = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

traicay = ("Táo", "Chuối", "Táo", "Cam", "Mận", "Dưa Hấu")

#3. Các thao tác với Tupple
# Chúng ta có thể truy cập nhiều mục bằng cách tham khảo số chỉ mục , bên trong dấu ngoặc vuông:

print(gioitinh[0])

print(traicay[0:2])

# Lưu ý giá trị phần tử của Tuple là không thể thay đổi 

# lophoc[0] = 13

# Duyệt từng phần tử bên trong Tuple bằng vòng lặp
for x in traicay:
    print(x)
    
# Cộng hai Tuple
y = (1,2,3) + (4,5,6)
print(y)

# Nhân hai Tuple
y = (1,2,3)*2
print(y)

# Sử dụng toán tử in để kiểm tra xem một phần tử có tồn tại trong bộ tuple hay không 
print("Táo" in traicay)

print("Bom" in traicay)

# Chúng ta có thể lấy số lượng phần tử của Tuple bằng hàm len()
x = len(traicay) # <= lenght độ dài
print(x)

# Đếm số lượt xuất hiện
print(traicay.count("Táo"))

print(traicay.count("Bom"))

# Tìm min, tìm max và tính sum
print(min(gioitinh))
print(max(traicay))
print(sum(lophoc))

# Sắp xếp Tuple và chuyển về List
listTC = sorted(traicay)
print(listTC)