# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:47:46 2024

@author: Alee
Bài số 33 Bài tập về Kế thừa trong Python
"""
"""
KẾ THỪA TRONGH PYTHON
* Mọi ngôn ngữ lập trình hướng đối tượng sẽ không đáng để xem hoặc sử dụng , nếu nó không hỗ trợ tính kế thừa

* Python hỗ trợ kế thừa

* Các lớp có thể kế thừa từ các lớp khác

* Một lớp có thể kế thừa các thuộc tính và phương thức hành vi từ một lớp khác, còn được gọi là lớp cha (lớp cơ sở hoặc lớp cha)

* Lớp kế thừa từ lớp cha được gọi là lớp con, còn được gọi là lớp thừa kế hoặc lớp con

"""
# Bài tập về động vật

class Animal:
    #Constructor: Xây dựng ra đối tượng
    def __init__(self, animaltypeA, nameA, widthA, heightA, weightA):
        self.animalType = animaltypeA
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight = weightA

    # phát ra âm thanh:
    def makevoice(self):
        print("Unknown voice")
        
    # in thông tin   
    def printMe(self):
        print("animeType: {0}, name={1} , width={2}, height={3}, weight={4}".format(self.animalType,self.name,self.width,self.height,self.weight))
        
a1 = Animal("Con Người", "Lê Hoàng Ân", " ", "170cm", "89kg")
a1.printMe()
a1.makevoice()
 
# Tạo class thừa kế
class Dog(Animal):
    #constructor của lớp con:
    def __init__(self, animaltypeA, nameA, widthA, heightA, weightA, isChampionA):
        # gọi constructor của lớp cha:
        Animal.__init__(self, animaltypeA, nameA, widthA, heightA, weightA,)
        # gán giá trị bổ sung
        self.isChampion = isChampionA 
    # override method
    def makeVoice(self):
        print("{0}: Gâu Gâu".format(self.name))
dog1 = Dog("Chó", "Cậu Vàng", "80cm", "40cm", "20kg", True)
dog2 = Dog("Chó" ,"Mật", "850cm", "100m", "50kg", True)
dog1.makeVoice()
dog1.printMe()
dog2.makeVoice()
dog2.printMe()

class Cat(Animal):
    #constructor của lớp con:
    def __init__(self, animaltypeA, nameA, widthA, heightA, weightA, colorA):
        # gọi constructor của lớp cha:
        Animal.__init__(self, "Cat", nameA, widthA, heightA, weightA)
        # gán giá trị bổ sung
        self.color = colorA 
    #override method
    def makeVoice(self):
        print("{0}: Meo Meo".format(self.name))
cat1 = Cat("CAT", "Mimi", "30cm", "10cm", "2kg", "Black")
cat2 = Cat("CAT","Tom", "80cm", "30cm", "20kg", "Blue")
cat1.printMe()
cat1.makeVoice
cat2.printMe()
cat2.makeVoice