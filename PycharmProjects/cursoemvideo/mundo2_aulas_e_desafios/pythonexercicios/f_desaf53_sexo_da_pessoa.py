sexo = str(input("\033[35mSexo da pessoa:\033[32m[M/F]")).upper().strip()[0]
while sexo not in "Mm/Ff":
    sexo = str(input("\033[31mSexo inválido!!.\033[m Tente novamente!! "))
print("\033[33mSexo \033[34m{} \033[33m aceito com sucesso.".format(sexo))
