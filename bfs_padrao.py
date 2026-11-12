class Grafo:
    def __init__(self):
        # Implementação utilizando Lista de Adjacência
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

    def busca_em_largura_padrao(self, inicio):
        if inicio not in self.adjacencia:
            return []

        fila = [inicio]
        visitados = []

        while len(fila) > 0:
            vertice = fila.pop(0)
            visitados.append(vertice)
            vizinhos = self.adjacencia[vertice]
          
            for vizinho in vizinhos:
                # i. Verificar se o vizinho não está na fila
                # ii. Verificar se o vizinho já não foi visitado
                if vizinho not in fila and vizinho not in visitados:
                    # iii. Adicionar o vizinho na Fila
                    fila.append(vizinho)

        # 4. Retornar Visitados
        return visitados

def main():
    grafo = Grafo()

    grafo.adicionar_aresta('A', 'B')
    grafo.adicionar_aresta('A', 'C')
    grafo.adicionar_aresta('B', 'D')
    grafo.adicionar_aresta('B', 'E')
    grafo.adicionar_aresta('C', 'F')
    grafo.adicionar_aresta('E', 'F')

    ordem_visitados = grafo.busca_em_largura('A')
    print(f"Ordem de visitação (BFS Padrão): {ordem_visitados}")


# Chamada explícita da função main
main()
