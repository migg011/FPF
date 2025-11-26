s_atual = float(input("digite seu salario atual: "))
porcentagem = float(input("digite sua porcetagem de reajuste: "))

s_novo = s_atual + (s_atual * (porcentagem / 100))

print("seu novo salario é de: ",s_novo)