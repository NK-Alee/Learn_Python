# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:50:29 2024

@author: Alee
Bài 16. Bài tập về tính diện tích và chu vi tam giác trong Lập trình Python
"""
"""
Nhập 3 điểm trên hệ trục tọa độ 0xy
1. Xác định 3 điểm có tạo thành tam giác không ?
2. Nếu tạo thành tam giác:
    2.a Xuất ra chu vi của tam giác
    2.b Xuất ra diện tích của tam giác
"""
# Sử dụng thư viên
import math
# Nhập dữ liệu
xA =float(input("Nhập vào xA: "))
yA =float(input("Nhập vào yA: "))
xB =float(input("Nhập vào xB: "))
yB =float(input("Nhập vào yB: "))
xC =float(input("Nhập vào xC: "))
yC =float(input("Nhập vào yC: "))


ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
bc = math.sqrt((xC-xB)**2 + (yC-yB)**2)
ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)

# Kiểm tra 
if (ab+bc > ac) and (ab+ac > bc) and (bc+ac > ab):
    print("Đây là hình tam giác")
    # Tính Chu Vi
    cv = ab+ac+bc
    print("Chu vi = ",cv)
    # Tính diện tích tam giác
    p = cv/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("Diện tích = ", s)
else:
    print("Không tạo thành tam giác")