#  Algoritmo de Bellman-Ford

## Introdução

O algoritmo de Bellman-Ford é um algoritmo de grafos utilizado para encontrar o menor caminho entre um vértice de origem e todos os outros vértices de um grafo ponderado.

Ele é muito importante na computação porque consegue trabalhar com pesos negativos nas arestas, algo que outros algoritmos, como o Dijkstra, não conseguem tratar corretamente.

Além disso, o Bellman-Ford também é capaz de detectar ciclos negativos, tornando-se extremamente útil em problemas de redes, roteamento e análise de caminhos.

---

# O que é um grafo?

Antes de entender o algoritmo, é importante compreender o conceito de grafo.

Um grafo é uma estrutura composta por:

- **Vértices (nós)** → representam pontos
- **Arestas** → representam conexões entre os pontos

Exemplo:

```txt
A ---- B
 \    /
   C
```

Nesse exemplo:
- `A`, `B` e `C` são vértices
- As linhas representam as arestas

Quando as arestas possuem valores numéricos, chamamos de **grafo ponderado**.

Exemplo:

```txt
A ----4---- B
 \         /
  2       1
   \     /
      C
```

Os números representam o custo/peso de cada caminho.

---

# Objetivo do algoritmo

O objetivo do Bellman-Ford é descobrir:

Qual o menor custo para sair de um ponto inicial e chegar aos outros pontos do grafo.

---

#  Como o algoritmo funciona

O Bellman-Ford funciona utilizando um processo chamado:

#  Relaxamento de arestas

Relaxar uma aresta significa:

> Verificar se existe um caminho menor passando por outro vértice.

---

##  Exemplo simples

Imagine que atualmente temos:

```txt
Distância até B = 10
```

Mas existe um caminho:

```txt
A → B com peso 3
```

E sabemos que:

```txt
Distância até A = 5
```

Então:

```txt
5 + 3 = 8
```

Como `8` é menor que `10`, atualizamos:

```txt
Distância até B = 8
```

Isso é o relaxamento.

---

#  Passo a passo do Bellman-Ford

##  Inicialização

O algoritmo começa definindo:

- Distância do vértice inicial = `0`
- Distância dos demais vértices = infinito

Exemplo:

| Vértice | Distância |
|---|---|
| A | 0 |
| B | ∞ |
| C | ∞ |
| D | ∞ |

---

##  Percorrer todas as arestas

O algoritmo percorre todas as arestas do grafo realizando relaxamentos.

Exemplo:

```txt
A → B = 4
A → C = 2
C → B = 1
```

Após relaxar:

| Vértice | Distância |
|---|---|
| A | 0 |
| B | 3 |
| C | 2 |

---

## Repetir o processo

O algoritmo repete o relaxamento:

```txt
V - 1 vezes
```

Onde:

- `V` = quantidade de vértices

Isso acontece porque o maior caminho possível sem ciclos possui `V - 1` arestas.

---

##  Verificação de ciclos negativos

Após terminar as repetições, o algoritmo faz mais uma passagem pelas arestas.

Se ainda for possível diminuir alguma distância:

Existe um ciclo negativo.

---

# O que é um ciclo negativo?

Um ciclo negativo ocorre quando a soma dos pesos de um ciclo é negativa.

Exemplo:

```txt
A → B = 2
B → C = -4
C → A = 1
```

Soma:

```txt
2 + (-4) + 1 = -1
```

Isso permite reduzir infinitamente o custo do caminho, tornando impossível encontrar uma menor distância válida.

---

# Complexidade do algoritmo

## Complexidade de Tempo

```txt
O(V * E)
```

Onde:

- `V` = número de vértices
- `E` = número de arestas

---

##  Comparação com Dijkstra

| Algoritmo | Pesos Negativos | Detecta Ciclo Negativo | Complexidade |
|---|---|---|---|
| Dijkstra | ❌ | ❌ | Mais rápido |
| Bellman-Ford | ✅ | ✅ | Mais lento |

---

#  Exemplo completo

## Grafo

```txt
A → B = 4
A → C = 2
C → B = 1
B → D = 5
C → D = 8
```

---

## Menor caminho partindo de A

```txt
A → C → B → D
```

---

## Cálculo

```txt
A → C = 2
C → B = 1
B → D = 5

Total = 8
```

---

# Exemplo básico em Python

```python
grafo = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('C', 'B', 1),
    ('B', 'D', 5),
    ('C', 'D', 8)
]

distancias = {
    'A': 0,
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf')
}

for _ in range(len(distancias) - 1):
    for origem, destino, peso in grafo:
        if distancias[origem] + peso < distancias[destino]:
            distancias[destino] = distancias[origem] + peso

print(distancias)
```

---

# ▶️ Como executar o projeto

## 1️⃣ Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2️⃣ Entrar na pasta do projeto

```bash
cd algoritmoBellmanFord
```

---

## 3️⃣ Executar o arquivo Python

```bash
python algoritmoBellmanFord.py
```

---

# Aplicações reais

O algoritmo de Bellman-Ford pode ser utilizado em:

- 🌐 Redes de computadores
- 📡 Protocolos de roteamento
- 🛰️ Sistemas de navegação e GPS
- 🧭 Problemas de caminho mínimo
- 📊 Sistemas de análise de grafos

---

#  Conceitos utilizados

Durante a implementação deste algoritmo são utilizados conceitos importantes como:

- Grafos
- Estruturas de dados
- Caminho mínimo
- Relaxamento de arestas
- Complexidade de algoritmos
- Laços de repetição
- Condicionais

---

# Tecnologias utilizadas

- Python
- Algoritmos e Estruturas de Dados

---

#  Objetivo acadêmico

Este projeto foi desenvolvido com fins acadêmicos para estudo de algoritmos de grafos, análise de caminhos mínimos e compreensão do funcionamento do algoritmo de Bellman-Ford.

---

#  Autor

Desenvolvido por Daniel Pacheco.
