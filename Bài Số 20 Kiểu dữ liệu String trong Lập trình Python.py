# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:33:08 2024

@author: Alee
Bài số 20 Kiểu dữ liệu String trong Lập trình Python
"""
# Ôn tập lại kiểu dữ liệu
a = 10
print(type(a))

b = 10.5
print(type(b))

c = True
print(type(c))

d = "Xin Chào"
print(type(d))

# Ví dụ chuỗi String
s1 = "Xin Chào"
s2 = "Alee"
s3 = s1 + " " + s2
print(s3)

# Ví dụ chuỗi String nhiều dòng bằng dấu nháy đơn '''
chuoi_nhieu_dong = ''' 
Dòng 1
Dòng 2 
Dòng 3
'''
print(chuoi_nhieu_dong)

# Ví dụ Lặp lại chuỗi string 
xin_chao = "Xin Chào Mấy Ní\n" # <= \n là ký tử dùng để xuống dòng trong chuỗi
xin_chao_10 = xin_chao*10
print(xin_chao_10)

# Ví dụ kiểm tra ký tự chuỗi có thuộc chuỗi khác  String
chuoi_1 = "Xin Chào Alee"
chuoi_2 = "Alee"
chuoi_3 = "VN"
if chuoi_2 in chuoi_1:
    print("Chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 2 không là chuỗi con của chuỗi 1")
    
if chuoi_3 in chuoi_1:
    print("Chuỗi 3 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 3 không là chuỗi con của chuỗi 1")    

# Ví dụ viết hoa chữ đầu tiên của chuỗi String 
s = "hôm nay trời đẹp quá !"
s = str.capitalize(s) # <= key .capitalize
print(s)

# Ví dụ viết hoa toàn bộ của chuỗi String
s = s.upper() # <= key .upper
print(s)

# Ví dụ viết thường toạn bộ của chuỗi String
s = s.lower() # <= key .lower
print(s)

# Ví dụ tìm và đếm số lượng chữ trong chuỗi String
s_2 = "Lập trinh Python là xu hướng hiện nay. Bạn nên học lập trình Python"
print(s_2.find("PythonX")) # Trả về -1 nếu không tìm thấy , ngược lại vị trí đầu tiên khi tìm thấy
print(s_2.find("Python"))
print(s_2.count("Python")) # <= Kiểm tra đếm số lượng chữ bằng key .count

# Ví dụ thay thế chữ trong chuỗi String
s_2 = s_2.replace("Python","PYTHON") # <= key .replace
print(s_2)

# Ví dụ cắt chuỗi thành một LIST trong chuỗi String
list1 = s_2.split(" ") # <= key .split
print(list1)

list2 = s_2.split(".")
print(list2)
# Ví dụ format của String
print("{0} + {1} = {2}".format(1, 2 , 1+2 ))

# Ví dụ lấy chuỗi con
print(s_2[0:10])