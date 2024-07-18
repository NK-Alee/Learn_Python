# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:42:46 2024

@author: Alee
Bài Số 28 Bài tập xây dựng chương trình tra từ điển
"""
"""
Bài Tập :
Xây dựng một từ điển, có các chức năng sau (người dùng lựa chọn chức năng thông qua menu):
1. Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào tử điển
2. Tra cứu ý nghĩa của một từ vựng
3. Cập nhật ý nghĩa cho một từ vựng.
4. Cho phép người dùng xóa đi một từ vựng trong từ điển.
5. Cho phép người dùng xóa toàn bộ từ vựng 
6. Cho phép người dùng in ra toàn bộ từ vựng
7. Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc : "TỪ VỰNG"  : "Ý NGHĨA"
8. Kết thúc chương trình 
"""

# Từ điện trống

tudien = {}

# Vòng lặp menu

while(True):
    print("------- MENU -------")
    print("1 - Thêm một từ vựng")
    print("2 - Tra cứu ý nghĩa một từ : ")
    print("3 - Cập nhật ý nghĩa cho một từ vựng")
    print("4 - Xóa từ vựng trong từ điển")
    print("5 - Xóa tất cả từ vựng trong từ điển")
    print("6 - In ra toàn bộ từ vựng đã lưu : ")
    print("7 - In ra toàn bộ từ vựng chi tiết có ý nghĩa")
    print("8 - Kết thúc chương trình")
    
    luachon=int(input("Lựa chọn chức năng:"))
    
    if(luachon == 1 or luachon == 3):
        tuvung = input("Nhập vào từ vựng muốn thêm:")
        ynghia = input("Nhập vào ý nghĩa:")
        tudien[tuvung] = [ynghia]
        print("Đã thêm hoặc cập nhật dữ liệu")
    elif(luachon == 2):
        tuvung = input("Nhập vào từ vựng cần tra từ:")
        print("Ý nghĩa:", tudien[tuvung])
    elif(luachon == 4):
        tuvung = input("Nhập vào từ vựng cần xóa:")
        tudien.pop(tuvung)
        print("Đã xóa dữ liệu")
    elif(luachon == 5):
        tudien.clear()
        print("Đã xóa toàn bộ từ điển")
    elif(luachon == 6):
        print("Danh sách các từ vựng có trong từ điển:")
        for x in tudien.keys():
            print(x)
    elif(luachon == 7):
        print("Danh sách các từ vựng có trong từ điển:")
        for x, y in tudien.items():
            print(x, ":", y)
    elif(luachon == 8):
        break
    else:
        print("Nhập lựa chọn không đúng!!")