# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:27:54 2024

@author: Alee
Bài Số 32 Bài tập Lập Trình Hướng Đối Tượng, phân biệt Method và Static Method
"""
"""
Lớp,Đối tượng, Thuộc Tính Và Phương Thức
1. Object : Đối Tượng
2. Class : Lớp
3. Method : Phương Thức
4. Inheritance : Kế Thừa
5. Polymorphism : Đa Hình
6. Encapsulation : Đóng Gói
7. Data Abstraction 

lỚP \ Đối Tượng :
Class : Một phạm trù đối tượng. Lớp định nghĩa tất cả các thuộc tính chúng ( thuộc tính và phương thức)
của các đối tượng khác nhau thuộc về nó. Các đối tượng, được tạo dựa trên định nghĩa của các lớp cụ thể
là một trong những tính năng chính của lập trình hướng đối tượng .

Bạn có thể đọc về ưu điểm và nhược điểm của lập trình hướng đối tượng tại đây:
https://www.roberthalf.com/blog/salaries-and-skills/4-domains-of-object-oriented-programming
https://www.softwareengineering.stackexchange.com/a/120038
http://www.freekpaans.nl/2015/06/exploring-the-essence-of-object-oriented-programming/

Dưới đây là một ví dụ về một lớp đơn giản, giúp bạn hiểu sự khác biệt giữa thuộc tính lớp và thuộc tình phần tử (trường hợp đơn lẻ của lớp)
class SimpleClass: < từ khóa class [tên_class]
i = 3 < thuộc tính attribute , có thể có nhiều class không có thuộc tính
def __init__(self): < def __init__ < hàm instance của class . (self) < bản thân của clas
    self.j = 7 
def printme(self):
    print(self.j)
"""
# Ví Dụ về tạo class đơn giản
class SimpleClass:
    # Attribute thuộc tính , biến toàn cục
    i = 5
    # hàm _Init_
    def __init__(self):
        self.j = 7
    # methods: Phương thức
    def printme(self):
        print(self.j)
objectA = SimpleClass()
objectB = SimpleClass()

objectA.printme()
print(objectB.i)

# Thay đổi giá trị của thuộc tính
objectA.i = 100
objectB.j = 500
print(objectA.i)
objectB.printme()

# Thử truy cập phương thức không phải static
#SimpleClass.printme()
# Báo lỗi

# Hướng dẫn về staticmethod < phương thức tĩnh
class SimpleClass2:
    # constructor
    def __init__(self):
        self.name="An"
        
    # methods
    def hello(self):
        print("Hello " + self.name)
        
    #static methods
    @staticmethod 
    def hi(name):
        print("Hi " + name);
objectC = SimpleClass2()
objectD = SimpleClass2()

objectC.hello()
objectC.hi("Peter")
SimpleClass2.hi("Ân Lê")

"""
Bài tập:
    Xây dụng Class ngay, thuộc tính gồm có : ngày, tháng, năm.
    Xây dụng các phương thức:
    + Cho biết đó là ngày thứ bao nhiêu trong năm.
    + Staticmethod: cho biết tháng đó có bao nhiêu ngày.
"""
class Ngay:
    # Constuctor
    def __init__(self, giatri_ngay, giatri_thang, giatri_nam):
        self.ngay = giatri_ngay
        self.thang = giatri_thang
        self.nam = giatri_nam
    # Xác định số ngày của tháng:
    @staticmethod
    def soNgayCuaThang(thang, nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif(thang in [4, 6, 9, 11]):
            return 30
        elif (thang==2):
            #return ((nam % 400 == 0)||(nam%4==0 && nam%100 !=0))?29:28;
            if (nam%400==0 or (nam%4==0 and nam%100 != 0)):
                return 29
            else:
               return 28
    # 15/03/2022
    # Tháng 1 : 31 ngày 
    # Tháng 2 : 28 ngày
    # 31 + 28 + 15 = ?
    def ngayTrongNam(self):
        giaTriNgayTrongNam = 0
    # Tính tổng số lượng ngày cững những tháng trước
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x, self.nam)
    # Công thêm số ngày của tháng hiện tại
        giaTriNgayTrongNam+=self.ngay
    # Trả kết quả
        return giaTriNgayTrongNam
            
ngayA = Ngay(20, 3, 2024)
print(ngayA.ngayTrongNam())
ngayB = Ngay(15, 1 ,2024)
print(ngayB.ngayTrongNam())