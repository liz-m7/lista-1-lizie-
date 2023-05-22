print("*******verificador de qual numero é maior*******")
num1=int(input("numero 1: \n"))
num2=int(input("numero 2: \n"))
num3=int(input("numero 3: \n"))

maior = num1
if num2>num1 and num2>num3:
    maior=num2
if num3>num1 and num3>num2:
    maior=num3
menor = num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num1 and num3<num2:
    menor=num3
    
print("o menor numero é o", menor) 
print("----programa finalizado----")
