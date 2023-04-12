{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP2ZdX3OWtIKWsmMNEGiVDf"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XK81iIPblADG",
        "outputId": "696351f4-2a00-424f-80bb-3c67df940a77"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Resultado esperado --->  [0, 0, 0, 1]\n",
            "------------------------------------------------------------------------\n",
            "Resultado final --->  [0, 0, 0, 1]\n",
            "------------------------------------------------------------------------\n",
            "Valores finais dos pesos --->  [0.1999999999999999, 0.8]\n",
            "------------------------------------------------------------------------\n",
            "Iteracoes --->  11\n"
          ]
        }
      ],
      "source": [
        "#------------------------------------\n",
        "# Instituto Federal do Espírito Santo\n",
        "#   Professora Mariana Rampinelli\n",
        "#    Disciplina: Redes Neurais\n",
        "#        Fernando Rosa Rocha\n",
        "#             Perceptron \n",
        "#-----------------------------------\n",
        "\n",
        "#Inicialiação dos vetores dos pesos e de x\n",
        "import random\n",
        "\n",
        "listx = [[0, 0, 1, 1], [0, 1, 0, 1]]\n",
        "vetw = [2, 1]\n",
        "atual = 0\n",
        "for i in range(0, len(vetw)):\n",
        "    vetw[i] = (random.randrange(1, 10))/10\n",
        "\n",
        "def perceptron(x, w):\n",
        "    vet = [0, 0, 0, 0]\n",
        "    u = -1\n",
        "    for i in range(0, 4):\n",
        "        for j in range(0, 2):\n",
        "            u = u + ((x[j][i])* w[j])\n",
        "            if (u > 0):\n",
        "                vet[i] = 1\n",
        "            else:\n",
        "                vet[i] = 0\n",
        "    return vet\n",
        "            \n",
        "v = perceptron(listx, vetw)\n",
        "\n",
        "#O vetor d é a entrada do sistema, que o perceptron deve encontrar no final das iterações\n",
        "\n",
        "def treinamento(v, x, w):\n",
        "    d = [0, 0, 0, 1] #VALOR A SER ENCONTRADO PELO PERCEPTRON NO FINAL\n",
        "    for i in range(0, 4):\n",
        "        for j in range(0, 2):\n",
        "            w[j] = (w[j] + 0.05*(d[i] - v[i])* x[j][i])\n",
        "    \n",
        "    v = perceptron(x, w)\n",
        "    return d, v, w\n",
        "          \n",
        "inicio = treinamento(v, listx, vetw)\n",
        "media = 1 #Variável auxiliar para o cálculo do erro\n",
        "cont = 0\n",
        "dif = 1\n",
        "\n",
        "while (dif != 0):\n",
        "    inicio = treinamento(inicio[1], listx, inicio[2])\n",
        "    cont = cont + 1\n",
        "    dif = 0 \n",
        "    for i in range(0,4):\n",
        "        dif = abs(inicio[0][i] - inicio[1][i]) + dif\n",
        "\n",
        "\n",
        "print(\"Resultado esperado ---> \", inicio[0])\n",
        "print(\"------------------------------------------------------------------------\")\n",
        "print(\"Resultado final ---> \", inicio[1])\n",
        "print(\"------------------------------------------------------------------------\")\n",
        "print(\"Valores finais dos pesos ---> \", inicio[2])\n",
        "print(\"------------------------------------------------------------------------\")\n",
        "print(\"Iteracoes ---> \", cont)"
      ]
    }
  ]
}