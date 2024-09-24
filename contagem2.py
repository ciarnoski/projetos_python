import time

entrada = int(input("Digite o tempo em minutos: ")) * 60
while entrada >= 0:
    minutos = entrada // 60
    segundos = entrada - (minutos * 60)
    print(f"{minutos:02}:{segundos:02}")
    time.sleep(1)
    entrada -= 1