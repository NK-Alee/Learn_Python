# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:18:16 2024

@author: Alee
Bài Số 29 Xây dựng Function trong Python
"""
"""
FUNCITION trong Python

Định Nghĩa :
* Hàm là một khối mã chỉ chạy khi nó được gọi .
* Bạn có thể truyền dữ liệu, được gọi là tham số, vào một hàm
* Kết quả là một hàm có thể trả về dữ liệu

Khai báo hàm:
Trong Python, một hàm được đĩnh nghĩa bằng từ khóa def : 
Ví dụ 
def xinchao():
    print("Xin chào!")
"""
#Gọi Hàm:
#Để gọi một hàm, hãy sử dụng tên hàm sau bởi dấu ngoặc đơn:
#    xinchao()

#Đối số (Arguments):
    #Hàm có thể nhận vào các tham số:
def xinchao(hovaten):
    print("Xin chào:" + hovaten)
xinchao("Lê Hoàng Ân")
    #Một hàm có thể nhận nhiều đối số:
def xinChao(ho, chulot, ten):
    print("Xin chào:" + ho + " " + chulot + " " + ten)
xinChao("Lê", "Hoàng", "Ân")
"""Nếu chung ta không biết có bao nhiêu đối số sẽ được truyền, chúng ta thêm một *
trước tên tham số trong định nghĩa hàm. Hàm sẽ nhận được nhiều đối số và có thể truy cập
các mục tương ứng:
"""
# Khi không xác định được đối số, chúng ta có thể sử dụng dấu *
def thoikhoabieu(*monhoc):
    print("Môn 1: " + monhoc[0])
    print("Môn 2: " + monhoc[1])
    print("Môn 3: " + monhoc[2])
    print("Môn 4: " + monhoc[3])
    print("Môn 5: " + monhoc[4])
    print("Môn 6: " + monhoc[5])
thoikhoabieu("Toán", "Lý", "Hóa", "Văn", "Sử", "Địa")

def tinhtong(*giatri):
    sum = 0
    for x in giatri:
        sum = sum + x
    print(sum)
    
tinhtong(1, 2)

tinhtong(1, 5, 7, 8, 9, 5)

# Sử dụng từ khoa chiếu đối số, thêm dấu ** vào trước tên tham số:

# Truyền nhiều đối số, xác định thông qua tên, sử dụng **

def xinchao2(**hovaten):
    print('Xin chào:'+ hovaten["ho"] + " " + hovaten["ten"])
    
xinchao2(ten="Ân", chutlot="Hoàng", ho="Lê")

#Sử dụng từ khóa "return" để trả về giá trị
def tinhTich(*giatri):
    tich = 1
    for x in giatri:
        tich = tich*x
        
    return tich

# Bài tập: Tìm USCLN của hai số a,b
# Xây dựng hàm: gcd(a,b) => trả về USCLN
# Ví dụ: 1, 13 => gcd (1,13)=> 1
# Ví dụ: 35, 77 => gcd(35,77)=>7
# Thuật toán đơn giản:
#35,42
#35,7
#28,7
#21,7
#14,7
#7,7
def gcd(a, b):
    while (a!=b):
        if (a>b):
            a = a - b
        else:
            b = b - a 
    return a

print(gcd(55,100))
print(gcd(11,121))

# Bài tập 2:
# Nhập vào một dãy (n) số từ bàn phím, sau đó tính tổng
# Yêu Cầu:
# Xây dụng các hàm:
# nhap(n, list_number)
# tinhtong(list_number)

# khai báo biến
list_number = []
n = -1
while(True):
    try:
        n = int(input("Nhập vào số lượng phần tử: "))
    except:
        print("Vui lòng nhập n>=1")
    if (n>=1):
         break
# hàm nhập()
def nhap(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập vào giá trị thứ " + str(i)+" : " )))
# ham tinh tong
def tinhtong(list_number):
    tong = 0
    for x in list_number:
        tong+=x
    return tong
nhap(n, list_number)
print("Tong = "+ str(tinhtong(list_number)))