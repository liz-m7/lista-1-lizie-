print(" CALCULE SE IMC")

peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura em metros: "))

imc=peso/(altura*altura)

if imc < 18.5:
    print("baixo peso")
elif imc <= 24.9:
    print("intervalo normal")
elif imc <=29.9:
    print("sobrepeso")
elif imc <=34.9:
    print("obesidade classe I")
elif imc <=39.9:
    print("obesidade classe II")
elif imc <=40:
    print("obesidade classe III")
    
print("------finalizado------")
