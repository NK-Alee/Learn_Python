# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:34:51 2024

@author: Alee
Bài Số 25 Kiểu dữ liệu Set trong Python
"""
"""
Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trữ
tập hợp các dữ liệu , 3 kiểu còn lại là List [], Tuple () và Dictionary {}, tất cả đều có chất lượng và cách sử dụng khác nhau

Set là tập hợp không có thứ tự,không được trùng nhau, không thể thay đổi * và không được lập chỉ mục. Lưu ý: Các mục set là không thể thay đổi,nhưng bạn có thể xóa các mục và thêm các mục mới

Sử dụng Set bằng cặp ngoặc { } 
"""
# Ví dụ tạo mới set
monhoc = {"Toán", "Lý", "Hóa"}
print(monhoc)

# Ví dụ duyệt danh sách phần tử bên trong Set
for x in monhoc:
    print(x)
    
# Ví dụ thêm phần tử vào SET
monhoc.add("Lịch Sử") 
print(monhoc)

hocthem = {"Anh Văn", "Đàn Piano"}
monhoc.update(hocthem)
print(monhoc) 

# Ví dụ thêm list vào Set
hocphudao = ["Võ thuật", "Múa", "Võ thuật"]
print(hocphudao)

monhoc.update(hocphudao)
print(monhoc)

#Ví dụ xóa phần tử trong Set

#sử dụng .remove khi xóa có phần tử trong list sẽ xóa không có sẽ báo lỗi
#monhoc.remove("Võ thuật")
#print(monhoc)

#sử dụng.discard khi xóa có phần tử trong list sẽ xóa không có sẽ bỏ qua và không báo lỗi
monhoc.discard("Toán")
print(monhoc)

#sử dụng pop() sẽ xóa phần tử đầu tiên trong set
monhoc.pop() 
print(monhoc)

#sử dụng .clear xóa tất cả phần tử bên trong set
#monhoc.clear()
#print(monhoc)

#sử dụng del [biến] xóa biến
del monhoc
print(monhoc)