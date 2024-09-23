def sequencia():
    for num in range(1,10+1):
        print(num)

sequencia()

x = 10 #escopo global

def exemplo():
    x = 15 #escopo local
    print(x) #esse print resultará em 15, pois dentro do def o x recebe outro valor
    y = 20

print(x) #o resultado dará 10, pois esse print() não está tabulado dentro do def
exemplo() #aqui é usado para chamar a função def
print(y) #não há como chamar uma varíavel local dessa forma, pois ela está apenas dentro da função def