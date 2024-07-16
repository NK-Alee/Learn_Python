# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:32:57 2024

@author: Alee
Bài 17 Kiểu dữ liệu List trong Lập trình Python
"""
"""
Giới thiệu kiểu dữ liệu List trong python
Ví dụ nhập từng biến
sv1 = "Tùng"
sv2 = "An"
sv3 = "Yến"
Số lượng sinh viên càng nhiều , biến càng nhiều gây tốn công khi code

List : (Danh Sách) là một chuỗi các mục có thứ tự. nó là một trong những kiểu dữ liệu được sử dụng nhiều nhất trong Python và rất linh hoạt .
Tất cả các mục trong danh sách không cần phải cùng loại

Khai báo một danh sách khá đơn giản. Các mục được phân tách bằng dấu phẩy được đặt trong dấu ngoặc [].
"""
# Tạo List Rỗng
emptylist = []

# Tạo ra một đối tượng list
emptylist2 = list()

print(emptylist)
print(emptylist2)

# Tạo ra List có dữ liệu
colors = ["red","green","orange"]
print(colors)

# List có thứ tự, vị trí các phần tử được đấu từ 0 , từ trái sang phải
studentList = ["An", "Bình", "Ngân", "Vi"]
print(studentList[3])
print(studentList[0])

# Gọi tất cả các phần tử
print(studentList)

# Gọi tất cả các phần tử bằng dấu :
print(studentList[:])

# studenList[1:2] => Lấy ra [1:2] > từ 1 tới nhỏ hơn 2
print(studentList[1:2])
print(studentList[0:2])
print(studentList[1:4])

# Thêm phân tử vào cuối hàm List : => .append  ten_ham.append(phần tử muốn thêm)
studentList.append("Thiên")
print(studentList)

# Thêm phần tử vào cuối hàm List : =>len ten_ham[len(ten_ham):] = ["ten_phan_tu"] 
studentList[len(studentList):] = ["Thành"] 
print(studentList)

# Thêm phần tử vào giữa hàm List : => .insert  ten_ham.insert(vi_tri_list,ten_phan_tu_muon_them) , vị trí ở hàm cũ khi chèn vào sẽ được đẩy lên ví dụ Ngân ở vị trí 2 sẽ được đẩy lên 3
studentList.insert(2, "Ngọc")
print(studentList)

# Đếm số lượng phần tử có trong list: => len (độ dài)
print(len(studentList))

# Đếm số lượng phần tử thỏa điều kiện : => .count ten_ham.count("dieu_kien") 
print("Đếm Ngọc:", studentList.count("Ngọc"))
print("Đếm Thành:", studentList.count("Thành"))
print("Đếm An:", studentList.count("An"))

#Kiểm tra điều kiện phần tử có bên trong list : => in trước khi xóa if "dieu_kien" in ten_ham:
if "Ngọc" in studentList:
       studentList.remove("Ngọc")
       print(studentList)

# Xóa phần tử ra khỏi List : => .remove ten_ham.remove(ten_phan_tu) , Nếu trùng tên sẽ xóa vị trí cũ nhất tới mới nhất
studentList.remove("Ngân")
print(studentList)

# Xóa phần tử ra khỏi List bằng vị trí : => .pop  ten_ham.pop(vị_trí_phần_tử)
studentList.pop(0)
print(studentList)

# Đảo ngược list : => .reverse  ten_ham.reverse()
studentList.reverse()
print(studentList)

# Sắp xếp phần tử lại từ a-z  : => .sort  ten_ham.sort()
studentList.sort()
print(studentList)

# Sắp xếp phần tử theo số [Number] từ nhỏ đến lớn : => .sort  ten_ham.sort() 
numbers = [7, 5, 1, 9, 0, 5, 7]
numbers.sort()
print(numbers)

# Sắp xếp phần tử từ cuối chữ cái đến đầu : => .sort(reverse=True)  ten_ham.sort(reverse=True)
studentList.sort(reverse=True)
print(studentList)

# Sắp xếp phần tử theo số [Number] giảm dần : => .sort(reverse=True)  ten_ham.sort(reverse=True)
numbers.sort(reverse=True)
print(numbers)

# Xóa sạch dữ liệu trong list : => .clear  ten_ham.clear()
studentList.clear()
print(studentList)