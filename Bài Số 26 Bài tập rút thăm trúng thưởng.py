# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:54:36 2024

@author: Alee
Bài số 26 Bài tâp rút thăm trúng thưởng
"""
"""
Ví dụ:
    -Mã căn cước công dân
    -Biển số xe
    -Số điện thoại
Bài tập:
    Xây dựng chương trình rút thăm trúng thưởng với các chức năng :
        1.Thêm một mã số dự thưởng vào thùng
        2.Xóa một mã số dự thưởng ra khỏi thùng
        3.Quay số ngẫu nhiên lấy ra một mã số trúng thưởng
"""
# Thư Viện Random
import random

# Khai báo set
thungphieu= set()

# Vòng lặp
while(True):
    print("------- MENU -------")
    print("Vui lòng lụa chọn chức năng: ") 
    print("1 - Thêm một số điện thoại vào thùng phiếu dự thưởng") 
    print("2 - Xóa một số điện thoại từ thùng phiếu dự thưởng")
    print("3 - Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng")
    print("4 - Kết thúc chương trình")
    print("Thùng phiếu hiện tại")
    print(thungphieu)
    
    
    luachon = int(input("Lựa Chọn: "))
    
    if(luachon ==1):
        sodienthoai = input("Nhập vào số điện thoại dự thưởng: ")
        thungphieu.add(sodienthoai)
    elif (luachon==2):
        sodienthoai = input("Nhập vào số điện thoại dự thưởng cần xóa: ")
        thungphieu.discard(sodienthoai)
    elif (luachon==3):
        index = random.randint(0,len(thungphieu))
        print("Vị trí trúng thưởng" + str(index))
        i = 0
        for x in thungphieu:
            if(i==index):
                break
            i = i + 1
        print("Chúc mừng SDT :" + x + "Đã trúng thưởng!")
        thungphieu.discard(x)
    else:
        break;
    x = input("Nhập phím bất kỳ để tiếp tục")
