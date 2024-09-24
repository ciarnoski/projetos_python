import time

segundos = int(input('Quantos segundos deseja esperar? '))

for i in range(segundos):
    print(segundos)
    segundos = segundos-1
    time.sleep(3)
