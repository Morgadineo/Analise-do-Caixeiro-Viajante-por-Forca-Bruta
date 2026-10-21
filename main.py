import itertools
import random
import numpy as np
import math
import time

def caixeiro_viajante_forca_bruta(matriz_distancias, cidade_inicial=0):
    num_cidades = len(matriz_distancias)
    cidades = list(range(num_cidades))
    cidades.remove(cidade_inicial)
    menor_distancia = float('inf')
    melhor_rota = None
    rotas = itertools.permutations(cidades)
    quantidade_rotas = 0

    print(f"-- INICIANDO ANALISE --")
    inicio = time.time()
    for permutacao in rotas:
        quantidade_rotas += 1
        rota_atual = [cidade_inicial] + list(permutacao) + [cidade_inicial]
        print(f"- ROTA: {rota_atual} -> ", end="")
        distancia_atual = 0
        
        for i in range(len(rota_atual) - 1):
            distancia_atual += matriz_distancias[rota_atual[i]][rota_atual[i+1]]
            
        print(distancia_atual)
            
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = rota_atual

    fim = time.time()
    print(f"{quantidade_rotas} rotas analizadas...")
    print(f"{fim - inicio:.4f} segundos")
    return melhor_rota, menor_distancia

def gerar_matriz_cidades(n):
    vals = np.random.randint(1, 100, size=(n, n))
    dist_matrix = (vals + vals.T) // 2
    np.fill_diagonal(dist_matrix, 0)

    return dist_matrix



# Exemplo de uso com 4 cidades
if __name__ == "__main__":
    print("===============================================")
    print("        Analise do Caixeiro Viajante           ")
    print("===============================================")

    n = int(input("Digite a quantidade de cidades: "))

    print(" - GERANDO MATRIZ DE CIDADES - ")
    matriz = gerar_matriz_cidades(n)
    print(matriz)
    print("\n------- CALCULANDO MELHOR ROTA -------")
    rota, custo = caixeiro_viajante_forca_bruta(matriz)

    print("\n== MELHOR ROTA ==")
    print(f"{rota} -> {custo}")
