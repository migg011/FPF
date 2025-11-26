def porcentagem(a, b):
    return (a * 100) / b

t_eleitores = int(input("o numero total de eleitores: "))
v_brancos = int(input("o numero total de votos brancos: "))
v_nulos = int(input("o numero total de votos nulos: "))
v_validos = int(input("o numero total de votos validos \n"))

p_brancos = porcentagem(v_brancos, t_eleitores)
p_nulos = porcentagem(v_nulos, t_eleitores)
p_validos = porcentagem(v_validos, t_eleitores)

print("a porcentagem de votos brancos é de: ",p_brancos)
print("a porcentagem de votos nulos é de: ",p_nulos)
print("a porcentagem de votos validos é de: ",p_validos)