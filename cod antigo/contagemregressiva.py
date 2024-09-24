import time

minutos = int(input("Quantos minutos deseja esperar? "))

def cronometro(minutos):
secs = minutos * 60

for tempo in range (secs, -1, -1):
min = tempo // 60
sec = tempo % 60
print(f'{min:02}:{sec:02}', end='\r')
time.sleep(1)

minutos = int(input("Digite os minutos: "))


cronometro(minutos)

###########################################################

import time

def cronometro(minutos):
for t in range(minutos * 60, -1, -1):
print(f'{t // 60:02}:{t % 60:02}', end='\r')
time.sleep(1)

minutos = int(input("Digite os minutos: "))
cronometro(minutos)

###########################################################

import time

for t in range(int(input("Digite os minutos: ")) * 60, -1, -1):
print(f'{t//60:02}:{t%60:02}', end='\r')
time.sleep(1)

###########################################################

import time;[time.sleep(1) or print(f'{t//60:02}:{t%60:02}', end='\r') for t in range(int(input(""))*60,-1,-1)]