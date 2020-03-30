"""
İkinci dereceden bir bilinmeyenli denklemin köklerini bulmak

Denklem : a * x^2 + b *x + c = 0

Delta : b ** 2 - 4 * a * c

Birinci kök : (-b - delta ** 0.5) / (2 * a)
İkinci kök : (-b + delta ** 0.5) /(2 * a)

"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b **2 -4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b -+ delta ** 0.5) / (2 * a)

print("Birinci Kök: {}\nİkinci Kök: {}".format(x1,x2))
