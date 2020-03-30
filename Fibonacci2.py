print(""" 
*******************************
Fibonacci serisi :  Serideki her sayı 
kendinden önceki iki sayının 
toplamıdır. Seri, 1 ve 1 ile başlar
Doğada pekçok sistem gizemli şekilde 
bu seriye uygun özellikler gösterir. 
******************************""")

a = 1
b = 1

fibonacci = [a , b]

for i in range(20):
        a,b = b, a+b

        fibonacci.append(b)

print(fibonacci)
