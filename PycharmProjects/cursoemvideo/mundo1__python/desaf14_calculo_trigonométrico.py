import math
ang = float(input("Digite um ângulo qualquer: "))
seno = math.sin(math.radians(ang))
print("O ângulo de {} tem o sin = {:.2f}".format(ang, seno))
cos = math.cos(math.radians(ang))
print("O ângulo de {} tem o cos = {:.2f}".format(ang, cos))
tan = math.tan(math.radians(ang))
print("O ângulo de {} tem o tan = {:.2f}".format(ang, tan))