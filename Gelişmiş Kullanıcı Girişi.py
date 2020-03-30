print("""
***********
Kullanıcı Girişi Programı
***********
""")

sys_kullanıcı_adı = "Cevat Prekazi"
sys_parola =  "987654321"

giris_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hataldıır")
        giris_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hataldıır")
        giris_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hataldıır")
        giris_hakkı -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı")
        break
    if(giris_hakkı == 0):
        print("Giriş Hakkınız Tükenmiştir")
        break