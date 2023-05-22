print(" BEM VINDO AO RESTAURANTE")
print("Cardapio do dia")
print("COMIDA...........PREÇO......codigo")
print("cachorro quente-R$1,20-------100")
print("bauru-----------R$1,30-------101")
print("hambúrgur-------R$1,20-------102")
print("cheeseburguer---R$1,30-------103 \n")
print("BEBIDA..........PREÇO--------codigo")
print("refrigerante----R$1,00-------104 \n")
print("para finalização da compra---111")


final = 0
while True:
c = int(input("Digite o codigo da comida que deseja: "))
    if(c == 111):
        break
qtd = int(input("Digite a quantidade desejada: "))




if c==100:
    final = 1.20*qtd
    
elif c==101:
    final = 1.30*qtd      
    
elif c==102:
    final = 1.20*qtd
    
elif c==103:
    final = 1.30*qtd
    
elif c==104:
    final = 1.0*qtd
    
print("seu pedido totalizou ",final, "reais")
