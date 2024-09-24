print("Nesse programa, vamos calcular o consumo médio de combustível, em km/L")
def combustivelmedio(a , b):
    media = a / b
    return media

n1 = float(input("Digite o total de quilometros percorridos nessa viagem: "))
n2 = float(input("Digite o total de combustível gasto durante sua viagem (em L): "))

print(f"A média de combustível gasto foi: {combustivelmedio(n1,n2)} km/L")


