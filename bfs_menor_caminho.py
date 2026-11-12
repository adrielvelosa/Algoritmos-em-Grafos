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

    def busca_em_largura_menor_caminho(self, inicio, destino):
        if inicio not in self.adjacencia or destino not in self.adjacencia:
            return None

        fila = [
            {
                'vertice': inicio,
                'caminho': [inicio]
            }
        ]
        
        visitados = []

        while len(fila) > 0:
            atual = fila.pop(0)
            vertice_atual = atual['vertice']
            caminho_atual = atual['caminho']

            if vertice_atual == destino:
                return caminho_atual

            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
                vizinhos = self.adjacencia[vertice_atual]

                for vizinho in vizinhos:
                    esta_na_fila = any(item['vertice'] == vizinho for item in fila)
                    
                    if not esta_na_fila and vizinho not in visitados:
                        fila.append({
                            'vertice': vizinho,
                            'caminho': caminho_atual + [vizinho]
                        })

        return None

def main():
    grafo = Grafo()

    grafo.adicionar_aresta('A', 'B')
    grafo.adicionar_aresta('A', 'C')
    grafo.adicionar_aresta('B', 'D')
    grafo.adicionar_aresta('B', 'E')
    grafo.adicionar_aresta('C', 'F')
    grafo.adicionar_aresta('E', 'F')

    menor_caminho = grafo.busca_em_largura_menor_caminho('A', 'F')
    print(f"Menor caminho de 'A' até 'F': {menor_caminho}")

main()
