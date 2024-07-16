# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:37:28 2024

@author: Alee
Bài số 23 Cách sử dụng câu lệnh break và continue trong Lập trinh Python
"""
"""
Câu lệnh ngắt Break Python
Câu lệnh  break kết thúc vòng lặp chứa nó. Điều khiển chương trình chuyển đến câu lệnh ngay sau phần thân của vòng lặp

Nếu câu lệnh break nằm trong một vòng lặp lồng nhau (vòng lặp bên trong một vòng lặp khác), câu lệnh break sẽ kết thúc vòng lặp trong cùng
"""
for i in range(0,11):
    print(i)
    if(i>4):
        print("vòng lặp đã đến 5 , ngưng chương trình")
        break

n = 100
while (n>0):
    print(n)
    n=n//2
    if(n<50):
        print("Đã chia tới 50 , Ngưng vòng lặp")
        break

for i in range(1,10):
    for j in range(2,10):
        print("{0}x{1}={2}".format(i, j, i*j))
        if (j>5):
            break
    print("\n")
    
"""
Câu lệnh continue trong Python
Câu lệnh continue được sử dụng để bỏ qua phần còn lại bên trong vòng lặp của lần lặp hiện tại
Vòng lặp không kết thúc nhưng tiếp tục với lần lặp tiếp theo
"""

for i in range(0,10):
    if(i%2==1):
        continue
    print(i)
    
"""
Continue là bỏ qua phần còn lại và thực thi vòng lặp tiếp theo
Break là ngắt ngang vòng lặp khi thỏa mãn điều kiện
"""