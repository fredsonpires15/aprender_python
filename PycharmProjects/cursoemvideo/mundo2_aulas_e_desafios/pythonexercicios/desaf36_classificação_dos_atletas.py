from datetime import date

nasc = int(input("\033[1:31mData de nascimento:"))
data = date.today().year
idade = data - nasc
print("\033[1:32mPara quem tem \033[1:39m{} anos;".format(idade))
if idade <= 9:
    print("Categória: \033[1:31m MIRIN!!")
elif 9 < idade <= 14:
    print("Categória: \033[1:32m INFANTIL!!")
elif 14 < idade <= 19:
    print("Categória: \033[1:33m JUNIOR!!")
elif 19 < idade <= 25:
    print("Categória: \033[1:34m SÉNIOR!! ")
elif idade > 25:
    print("Categória: \033[1:35m MASTER!! ")