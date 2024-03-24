from datetime import date
#  este programa diz se a pessoa pode se alistar para o serviço militar ou não
nasc = int(input("\033[33:1m Diga a sua data de nascimento?\033[m"))
print("""\033[44:30m [1] \033[m -» \033[1:37m Homem
\033[45:30m [2] \033[m -» \033[1:37m Mulher """)
sexo = int(input("\033[40:39m Sexo: \033[m"))
datual = date.today().year
idade = datual - nasc
print("\033[1:37m Para quem nasceu em \033[32m{} \033[m"
      "\033[1:37m tem \033[32m{}\033[m anos\033[1:37m em\033[m"
      " \033[32m{}".format(nasc, idade, datual))
if idade == 18 and sexo == 1:
    print("\033[1:36m O serviço militar para homem é obrigatório.\033[m")
    print("\033[1:31m Deve se alistar IMEDIATAMENTE!!\033[m")
elif idade < 18 and sexo == 1:
    print("\033[1:36m O serviço militar para homem é obrigatório.\033[m")
    f = 18 - idade  # tempo que falta para o alistamento
    ano = datual + f
    print("\033[1:31m Ainda fantam \033[32m{}\033[m ano(s)"
          " \033[1:31m para o alistamento, será em \033[32m{}\033[m!!".format(f, ano))
elif idade > 18 and sexo == 1:
    print("\033[1:36m O serviço militar para homem é obrigatório.\033[m")
    p = idade - 18  # tempo que passou para o alistamento
    ano = datual - p
    print("\033[1:31m Você deveria ter se alistado desde \033[32m{}\033[m,"
          " \033[1:31m já se passam \033[32m {} ano(s)!!\033[m".format(ano, p))
elif sexo == 2:  # para as mulheres
    print("\033[1:35m O serviço militar para as mulheres não é obrigatório\033[m")
else:
    print("\033[1:31m Não existe esta opção.\033[m Por favor, Tente novamente!!")