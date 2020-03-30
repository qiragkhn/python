print("""
******************************************
ATM Makinesine Hoşgeldiniz

İşlemler: 

1- BAkiye Sorgulama
2- Para Yatırma
3- Para Çekme 

Progrmadan çıkmak için X tuşuna basınız. 
******************************************
""")

bakiye = 1000

while True:
    işlem = input("İşlem Numarası Seçiniz: ")

    if (işlem == "x"):
        print("Yine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz Miktarı Giriniz: "))

        bakiye += miktar
        print("Yeni Bakiyeniz {} TL'dir".format(bakiye))
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz Miktar Giriniz: "))
        bakiye2 = bakiye - miktar
        print("Yeni Bakiyeniz {} TL'dir".format(bakiye2))

        if (bakiye - miktar < 0):
            print("Bu işlem için yeterli bakiyeniz yoktur")
            continue
    else:
        print("Geçersiz İşlem")