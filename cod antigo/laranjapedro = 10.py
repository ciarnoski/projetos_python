laranjapedro = 10
print("Pedro tem 10 laranjas")
laranjasroubadas = int(input("Retire quantas laranjas você quiser de Pedro: "))
if laranjapedro - laranjasroubadas >= 5:
    print("Pedro está feliz")
elif laranjapedro - laranjasroubadas < 5 and laranjapedro - laranjasroubadas > 0:
    print("Pedro está decepcionado")
elif laranjapedro - laranjasroubadas < 0:
    print("Pedro não tem tudo isso de laranjas!")
  
