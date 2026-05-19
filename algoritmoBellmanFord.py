#=========================
#ALGORITMO DE BELLMAN-FORD
#=========================


def bellman_ford(vertices, arestas, origem):
#inicializa distancias
    distancias = {}
    for v in vertices:
        distancias[v] = float('inf')
        distancias[origem] = 0

#Relaxamento das Arestas

for i in range(len(vertices)-1):
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            distancias[v] = distancias[u] + peso

#Verifica clico negativo

for u, v, peso in arestas:
    if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
        print ("\nO grafo possui ciclo negativo!")
        return None
    return distancias

#=========================
#ENTRADA DE DADOS
#=========================

vertices = []
arestas = []

qtd_vertices =(input("Quantidade de vertices: "))


for i in range(qtd_vertices):
    vertice = input(f"Nome da vertice {i+1}: ")
    vertices.append(vertice)

qtd_arestas = int (input("Quantidade de arestas: "))
for i in range (qtd_arestas):
    origem = input ("Origem: ")
    destino = input ("Destino: ")
    peso = int(input("Peso da aresta: "))
    arestas.append((origem, destino, peso))

#=========================
#EXECUÇÃO
#=========================        

origem = input("Vertice inicial: ")
resultado = bellman_ford(vertices, arestas, origem)

#=========================
#SAIDA
#=========================

if resultado:
    print("\nMenores Distancias: ")
    for vertices in resultado:
        print("f{origem} -> {vertice} = {resultado[vertice]}")
