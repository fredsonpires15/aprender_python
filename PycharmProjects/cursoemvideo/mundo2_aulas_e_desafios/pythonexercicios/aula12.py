import emoji
nome = str(input("Digite seu nome:")).strip()
if nome == "Fredson".capitalize():
    print("É um prazer te conhecer,\033[34m {}\033[m, o seu nome nome é muito bonito!".format(nome))
elif nome == "Pedro" or nome == "João" or nome == "Fredy":
    print("Seu nome é muito popular em portugal!!")
else:
    print("Seu nome é bem normal!!")
print(emoji.emojize("Tenha um bom dia \033[36m{}\033[m!"
                    "\033[33m:sun_with_face:\033[m"
                    " \033[32m:herb:\033[m "
                    "\033[31m:hibiscus:\033[m "
                    "\033[33:40m :relieved:\033[m".format(nome), language="alias"))
