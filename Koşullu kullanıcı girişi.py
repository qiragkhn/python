print("""____________
Kullanıcı Girişi
__________
""")

sys_kullanıcı_adı = "Gökhan"
sys_parola = "123456"

kullanıcı_adı = input("kullanıcı adı :  ")
parola = input ("Parola : ")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı....")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı adı hatalı....")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Böyle bir kullanıcı bulunmamaktadır")
else:
    print("Sisteme başarıyla giriş yapılıyor")