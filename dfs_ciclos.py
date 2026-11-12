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

    def detectar_ciclos(self, inicio):
        if inicio not in self.adjacencia:
            return False

        pilha = [
            {
                'vertice': inicio,
                'pai': None
            }
        ]
        visitados = []

        while len(pilha) > 0:
            atual = pilha.pop()
            vertice_atual = atual['vertice']
            pai_atual = atual['pai']

            visitados.append(vertice_atual)

            for vizinho in self.adjacencia[vertice_atual]:
                esta_na_pilha = any(item['vertice'] == vizinho for item in pilha)

                # Se não está na pilha e não foi visitado, empilha com o vértice atual como pai
                if not esta_na_pilha and vizinho not in visitados:
                    pilha.append({
                        'vertice': vizinho,
                        'pai': vertice_atual
                    })
                # Se já está na pilha ou visitado e não é o pai, há um ciclo
                elif vizinho != pai_atual:
                    return True

        return False

def main():
    grafo_com_ciclo = Grafo()
    grafo_com_ciclo.adicionar_aresta('A', 'B')
    grafo_com_ciclo.adicionar_aresta('B', 'C')
    grafo_com_ciclo.adicionar_aresta('C', 'A')

    print(f"Grafo 1 possui ciclo? {grafo_com_ciclo.detectar_ciclos('A')}")

    grafo_sem_ciclo = Grafo()
    grafo_sem_ciclo.adicionar_aresta('A', 'B')
    grafo_sem_ciclo.adicionar_aresta('B', 'C')
    grafo_sem_ciclo.adicionar_aresta('B', 'D')

    print(f"Grafo 2 possui ciclo? {grafo_sem_ciclo.detectar_ciclos('A')}")

main()
