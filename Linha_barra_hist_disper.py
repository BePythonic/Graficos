from matplotlib import pyplot as plt # Todos os graficos abaixo usam pyplot
from collections import Counter      

#Indice
#Grafico de Linha - l.14
#Grafico de Barras - l.33
#Histograma em decil -l.56
#Grafico de dispersao simples -l.79
#Apendice 1 - Usando o Enumerate - l.l87
#Apendice 2 - Usando uma funcao lambda - l.111 
#Apendice 3 - Usando o collections.Counter - l.136


# -------------------- Grafico de Linha --------------

# Eh necessario duas listas, uma representando o eixo x e outra o eixo y, ambas com 
# o mesmo numero de elementos.
eixox = [1,2,3,4,5 ]
eixoy = [2,4,6,8,10]
# Cria um grafico de linha
plt.plot(eixox,eixoy,color="green",marker="o",linestyle="solid")

#Adiciona Titulo ao grafico
plt.title("Grafico de linha")

#Adiciona um label nos eixos
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

#Comando necessario para exibir o grafico
plt.show()

# -------------------- Grafico de barras -------------

#Eh necessario duas listas, uma representando o conjunto discreto de itens e outra 
#representando os valores numericos associados a esses itens.

itens =  ["item1","item2","item3","item4"]
valores=[10,20,5,12] #10 item1, 20 item2, 5 item3 e 12 item4
#Eh preciso enumerar os itens uma vez que a ordem de exibicao eh totalmente arbitraria
xs = [i for i,_ in enumerate(itens)] # Ver Apendice 1- Funcionamento do enumerate
# dai basta criar o grafico
plt.bar(xs,valores)

#Adicionar Label no eixo y e dar titulo ao grafico
plt.ylabel("Valores")
plt.title("Grafico de barra")

#Troca os numeros xs pelos nomes item1, item2 e etc

plt.xticks([i for i,_ in enumerate(itens)],itens)

#Mostrar o grafico
plt.show()

# -------------Histograma de frequencias absolutas dividido em decil -------------------

#Eh necessario ter uma lista com os valores observados

valobs = [5,8,9,42,31,69,65,62,74,71,85,91,95,97,1,1]
decil = lambda val: (val//10)*10 # Ver Apendice 2-Como funciona uma funcao lambda

histogram = Counter(decil(val) for val in valobs) # Ver apendice 3-Como funciona o Counter 
#from collections

#Cria o histograma
plt.bar([x for x in histogram.keys()], histogram.values(), 10) # 10 eh a largura de cada barra

plt.axis([-5,105,0,10]) # eixo x de -5 a 105 eixo y(contagem) de 0 a 10

plt.xticks([10*i for i in range(10)]) # afinal sao 10 faixas de valores

#labels e titulo
plt.xlabel("Decil")
plt.ylabel("# de alunos")
plt.title("Histograma")
plt.show()

# -------------Grafico de dispersao - Scatter Plot Sem labels-------------------
#Eh preciso fornercer 2 listas

eixox = [1,2,3,4,5]    
eixoy = [200,50,23,154,32]
plt.scatter(eixox,eixoy) # se nao desejar colocar labels definir os 2 eixos e essa linha bastam
plt.show()

# Apendice 1 - Funcionamento do enumerate

# Suponha que voce tem uma lista com 4 nomes

lista = ["Alex","Brian","Carlos","Drax"]
tupla = ("Jorge","Lula","Bolsonaro")
#Se usar enumerate

e = enumerate(lista)
k = enumerate(tupla)
#Agora podemos iterar sobre os itens da lista
#Por exemplo, printando todos os itens

for index,item in e:
	print(item)  # Resultado disso sera Alex Brian Carlos Drax

# Ou printando os indices fazendo print(index)

# o mesmo funciona para tuplas
for _,item in k:
	print(item)
# Portanto quando fizemos xs = [i for i,_ in enumerate(itens)] ao criar o grafico de barras
# nos estavamos criando uma lista apartir dos indices dos itens que formam o grafico de barra.

#Apendice 2 - Como funciona uma funcao lambda?
# Funcao lambda, tambem conhecida como funcao anonima eh uma funcao que nao esta atrelada
# a nenhum nome
# Ex1.

f = lambda x: x+1
g = lambda y: y*2
print(f(5)) # 6
print(f(7)) #8

print(g(2)) #4
print(g(6)) #12

# Lambdas sao especialmente uteis para passar funcoes para funcoes
# quando fizemos decil = lambda val: (val//10)*10 criamos uma funcao chamada
# decil que toma um argumento, por exemplo, 79, pega a divisao inteira dele por 10, ficando com 7 
# e entao multiplica por 10 para obter 70, ou seja, uma funcao que mapeia um numero
# em seu decil. 79 --> 70, 55 -->50 e assim por diante.
# entao criamos uma lista (decil(val) for val in valobs) e usamos o Counter (Ver apendice 3)
# para contar a ocorrencia em cada decil.

# Portanto para as aplicacoes mais simples, lambda eh uma funcao rapida, que pode ser obtida
# fazendo f = lambda argumento: alguma conta com o argumento e dai usamos a funcao fazendo
# f(argumento) ---> a conta com o argumento .

#Apendice 3 - Usando o Counter

# Ao fazermos Counter(lista) obtermos uma especie de dicionario no qual os itens da lista sao
# guardados nas chaves .keys() e a frequencia absoluta de cada elemento e guardada nos valores .values()
# Ex
lista = [1,1,1,2,2,3,3,"Eu","Eu"]
d = Counter(lista)
print(d) # { 1:3,"Eu":2,2:2,3:2}

print(d.keys()) # gera lista com os itens
print(d.values()) # gera lista com as respectivas contagens
# Portanto eh facil ver a razao de usarmos Counter na construcao de um histograma
# Basta entender que Counter(lista) gera um dicionario com os itens da lista na chave e
# a frequencia absoluta de cada item no valor associado a chave.

