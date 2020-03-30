print("""
**************************
Faktöriyel bulma programı 

çıkmak için x'e basınız. 
**************************""")

while True:
    sayı = input("sayı:")
    if (sayı == "q") :
        print("Program sonlandırılıyor...")
        break

    else:
        sayı = int(sayı)

        factoriyel = 1

        for i in range(2,sayı+1):
            print("factoriyel", factoriyel, "i: ",i)
            factoriyel *= i
        print("sayının factoriyeli:", factoriyel)
        print("_______________")
