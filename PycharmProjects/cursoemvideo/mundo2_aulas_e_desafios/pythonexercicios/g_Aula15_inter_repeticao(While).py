"""n = s = 0
while n != 999:
    n = int(input("Digite um número:"))
    s += n
s -= 999
print(f"A soma foi {s}")"""

# Fazendo agora com lup infinito

n = s = c = 0
while True:
    n = int(input("Digite um número:"))
    if n == 999:
        break
    c += 1
    s += n

print(f"A soma dos {c} números digitados foi {s}")

