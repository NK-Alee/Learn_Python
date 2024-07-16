# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:02:55 2024

@author: Alee
Bài 11. Các toán tử gán trong lập trình Python
"""
"""
1. Toán Tử Gán
Toán tử gán được sử dụng trong Python để gán trị cho các biến
a = 5 là một toán tử gán đơn giản chỉ định giá trị 5 ở bên phải cho biến một bên trái
Có nhiều toán tử ghép khác nhau trong Python , ví dụ a + 5 tương đương với a = a + 5

Toán Tử - Ví Dụ - Tương Đương
= - a = 9 - a = 9

+= - a += 9 - a = a + 9 ( cộng )

-= - a -= 9 - a = a - 9 ( trừ )

*= - a *= 9 - a = a * 9 ( nhân )

/= - a /= 9 - a = a / 9 ( chia )

%= - a %= 9 - a = a % 9 ( chia lấy phần dư )

//= - a //= 9 - a = a // 9 ( chia lấy phần nguyên )

**= - a **= 9 - a = a ** 9 ( quỹ thừa )

&= - a &= 9 - a = a & 9 (bit)

|= - a |= 9 - a = a | 9 ( hoặc )

^= - a ^= 9 - a = a ^ 9

>>= - a >>= 9 - a = a >> 9

<<= - a <<= 9 - a = a << 9

2. Toán Tử bit
Toán tử bit hoạt động trên các toán hạng các chữ số nhị phân
Toán Tử - Ví Dụ - Tương Đương
& - a & b - Bitwise AND

| - a | b - Bitwise OR

^ - a ^ b - Bitwise XOR (exclusive OR)

~ - ~a - Bitwise NOT

<< - a << n - Bitwise left shift

>> - a >> n - Bitwise right shift

3. Toán tử đặc biệt
Toán Tử - Ý Nghĩa - Ví Dụ
is - Đúng nếu các toán hạng giống hệt nhau ( tham chiếu đến cùng một đội tượng) - x là đúng

is not - Đúng nếu các toán hạng không giống nhau ( không tham chiếu đến cùng một đối tượng) - x không đúng

