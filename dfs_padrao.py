class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino, direcionado=False):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencia[origem].append(destino)
        if not direcionado:
            self.adjacencia[destino].append(origem)

    def busca_em_profundidade(self, inicio):
        if inicio not in self.adjacencia:
            return []

        pilha = [inicio]
        visitados = []

        while len(pilha) > 0:
            # Retira o último elemento inserido (comportamento de Pilha)
            vertice = pilha.pop()
            visitados.append(vertice)

            for vizinho in self.adjacencia[vertice]:
                if vizinho not in pilha and vizinho not in visitados:
                    pilha.append(vizinho)

        return visitados


def main():
    grafo = Grafo()

    grafo.adicionar_aresta('A', 'B')
    grafo.adicionar_aresta('A', 'C')
    grafo.adicionar_aresta('B', 'D')
    grafo.adicionar_aresta('B', 'E')
    grafo.adicionar_aresta('C', 'F')
    grafo.adicionar_aresta('E', 'F')

    ordem_visitados = grafo.busca_em_profundidade('A')
    print(f"Ordem de visitação (DFS Padrão): {ordem_visitados}")


main()
