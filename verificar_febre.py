temperatura = float(input("Qual a temperatura corporal?"))
if(temperatura < 37.3):
    print("Paciente sem febre") 
elif(temperatura >= 37.3 and temperatura <= 37.8):
    print("Paciente febril") 
else: 
    print("Paciente com febre") 
