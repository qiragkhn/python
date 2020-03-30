print(""" ****************************************
HESAP Makinesi Programı 

İşlemler: 

1. Toplama işlemi 
2. Çıkarma işlemi 
3. Çarpma işlemi
4. Bölme işlemi 

***************************************
""")

x = float(input("Birinci sayıyı giriniz = "))
y = float(input("ikinci sayıyı giriniz ="))

işlem = input("İşlem numarası giriniz")

if işlem == "1":
    print("{} ile {}' in toplamı = {}' dir".format(x,y,x+y))
elif işlem == "2":
    print("{} ile {}' nin farkı = {}' dir".format(x,y,x - y))
elif işlem == "3":
    print("{} ile {}' nin çarpımı = {}' dir".format(x, y, x * y))
elif işlem == "4":
    print("{} ile {}' nin bölümü = {}' dir".format(x, y, x / y))
else:
    print("farklı biri şlem giridniz")