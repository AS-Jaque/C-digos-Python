lista = ["Ana" , "Pedro" , "Julia" , "Abner" , "Paula" , "Juliana"]


while True:
    consultarInscrito = str.capitalize(input("Digite o nome ou 0 para sair: "))

    if consultarInscrito == "0":
        break

    if consultarInscrito in lista:
        print("{} está inscrito(a)!".format(consultarInscrito))
    else:
        print("{} não está inscrito(a)!".format(consultarInscrito))
