#------------------------------------
# Instituto Federal do Espírito Santo
#   Professora Mariana Rampinelli
#    Disciplina: Redes Neurais
#        Fernando Rosa Rocha
#             Perceptron 
#-----------------------------------

#Inicialiação dos vetores dos pesos e de x

vetx = [2, 1, 2, 1]
vetw = [2, 1, 0.4, 0.7]
atual = 0

def perceptron(x, w):
    vet = [0,0,0,0]
    u = 1
    for i in range(0,4):
        u = u + ((x[i])* w[i])
        if (u >= 0):
            vet[i] = 1
        else:
            vet[i] = 0
    return vet
            
v = perceptron(vetx, vetw)

#O vetor d é a entrada do sistema, que o perceptron deve encontrar no final das iterações

def treinamento(v, x, w):
    d = [0, 1, 1, 1] #VALOR A SER ENCONTRADO PELO PERCEPTRON NO FINAL
    erro = [1, 1, 1, 1]
    for i in range(0,4):
      if(v[i] != d[i]):
          erro[i] = 1
          w[i] = (w[i] + 0.1*(d[i] - v[i])*x[i])
      else:
          erro[i] = 0
    
    v = perceptron(x, w)
    return d, v, w, erro
          
inicio = treinamento(v, vetx, vetw)
media = 1 #Variável auxiliar para o cálculo do erro
cont = 0

#Laço de repetição até que o erro seja zerado.
while(media != 0):
    inicio = treinamento(inicio[1], vetx, inicio[2])
    cont = cont + 1
    media = 0
    for j in range(0,4):
        media = media + ((inicio[3][j]))

print("Resultado esperado ---> ", inicio[0])
print("------------------------------------------------------------------------")
print("Resultado final ---> ", inicio[1])
print("------------------------------------------------------------------------")
print("Valores finais dos pesos ---> ", inicio[2])
print("------------------------------------------------------------------------")
print("Vetor erro na posicao (0 para correspondente | 1 para nao correspondente) ---> ", inicio[3])
print("------------------------------------------------------------------------")
print("Iteracoes ---> ", cont)




    


