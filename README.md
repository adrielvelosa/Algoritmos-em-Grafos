# Algoritmos em Grafos - Busca em Largura (BFS) e Busca em Profundidade (DFS)

## Integrantes do Grupo
* Adriel Velosa - 2022901
* Carolina Froehlich - 2025999
* Leonardo Laudelino - 2034248
* Emily Camila de Lima - 1989842

---

## Sobre o Projeto
Projeto acadêmico desenvolvido em **Python** para a disciplina de Estruturas de Dados / Teoria dos Grafos, contendo a implementação de uma estrutura de **Grafo** baseada em **Lista de Adjacência** e os principais algoritmos de percurso e análise.

## Estrutura do Repositório

Para manter a organização das entregas avaliativas, cada conjunto de algoritmos está isolado em sua respectiva *branch*:

### 1. Branch [`busca-em-largura`](../../tree/busca-em-largura)
Contém as implementações referentes à **Busca em Largura (Breadth-First Search - BFS)** utilizando estrutura de **Fila**:
* **`bfs_padrao.py`**: Percorre o grafo em níveis a partir de um vértice inicial e retorna a ordem completa dos vértices visitados.
* **`bfs_menor_caminho.py`**: Adapta a fila para armazenar o histórico do trajeto (`{'vertice': ..., 'caminho': ...}`), encontrando o menor caminho em número de arestas entre um vértice de origem e um de destino.

### 2. Branch [`busca-em-profundidade`](../../tree/busca-em-profundidade)
Contém as implementações referentes à **Busca em Profundidade (Depth-First Search - DFS)** utilizando estrutura de **Pilha**:
* **`dfs_padrao.py`**: Explora o grafo avançando o máximo possível em cada ramificação antes de retroceder, retornando a lista de vértices visitados.
* **`dfs_ciclos.py`**: Adapta a pilha para rastrear o vértice anterior (`{'vertice': ..., 'pai': ...}`), permitindo identificar a existência de ciclos no grafo.

## Como Executar

1. Clone o repositório e acesse a pasta do projeto:

    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>

2. Selecione a *branch* desejada e execute o arquivo correspondente:

* **Para Busca em Largura (BFS):**

      git checkout busca-em-largura
      python bfs_padrao.py
      python bfs_menor_caminho.py

* **Para Busca em Profundidade (DFS):**

      git checkout busca-em-profundidade
      python dfs_padrao.py
      python dfs_ciclos.py
