#Exercicio 1
# nome = input("Digite seu nome: ")
# print(f"Olá {nome}, seja bem vindo!")

# #Exercicio 2
# numero = int(input("Digite o número: "))
# if numero%2 == 0 :
#     print("Esse número é par")
# else:
#     print("Esse número é ímpar")

# #Exercicio 3
# listanomes = []

# for i in range(1,4):
#     i = input("Digite o nome: ")
#     listanomes.append(i)

# for n in listanomes:
#     print(n)

#Função
def adiciona_nomes_na_lista(ls):
    ls.append(input("Digite um nome: "))
def remove_nomes_na_lista(ls):
    ls.remove(input("Digite o nome: "))
    print(ls)

menu = 1
listanomes = []
while menu==1:
     print("Oque você quer fazer?")

     print("1. Adicionar nomes")
     print("2. Remover nome")

     escolha = input("Digite uma opção: ")

     if escolha == "1":
         adiciona_nomes_na_lista(listanomes)
         menu+=1
         print(listanomes)
     elif escolha == "2":
         remove_nomes_na_lista(listanomes)
         menu+=1
         print(listanomes)
     else:
         print("Inválido, tente novamente")