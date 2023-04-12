#Inicialiação dos vetores dos pesos e de x
import random

listx = [[0, 0, 1, 1], [0, 1, 0, 1]]
vetw = [2, 1]
atual = 0
for i in range(0, len(vetw)):
    vetw[i] = (random.randrange(1, 10))/10

def perceptron(x, w):
    vet = [0, 0, 0, 0]
    u = -1
    for i in range(0, 4):
        for j in range(0, 2):
            u = u + ((x[j][i])* w[j])
            if (u > 0):
                vet[i] = 1
            else:
                vet[i] = 0
    return vet
            
v = perceptron(listx, vetw)

#O vetor d é a entrada do sistema, que o perceptron deve encontrar no final das iterações

def treinamento(v, x, w):
    d = [0, 0, 0, 1] #VALOR A SER ENCONTRADO PELO PERCEPTRON NO FINAL
    for i in range(0, 4):
        for j in range(0, 2):
            w[j] = (w[j] + 0.05*(d[i] - v[i])* x[j][i])
    
    v = perceptron(x, w)
    return d, v, w
          
inicio = treinamento(v, listx, vetw)
media = 1 #Variável auxiliar para o cálculo do erro
cont = 0
dif = 1

while (dif != 0):
    inicio = treinamento(inicio[1], listx, inicio[2])
    cont = cont + 1
    dif = 0 
    for i in range(0,4):
        dif = abs(inicio[0][i] - inicio[1][i]) + dif


print("Resultado esperado ---> ", inicio[0])
print("------------------------------------------------------------------------")
print("Resultado final ---> ", inicio[1])
print("------------------------------------------------------------------------")
print("Valores finais dos pesos ---> ", inicio[2])
print("------------------------------------------------------------------------")
print("Iteracoes ---> ", cont)
