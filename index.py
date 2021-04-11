from collections import deque
INFINITO = float("inf")


class meu_grafo:
    def __init__(self, nome_do_meu_arquivo):

        arestas = []
        data = open(nome_do_meu_arquivo)
        for linha in data.readlines():  
            no_de, no_para, peso, *_ = linha.strip().split(" ")
            arestas.append((no_de, no_para, float(peso)))

        self.no = set()
        for aresta in arestas:
            self.no.update([aresta[0], aresta[1]])

        self.lista_de_adjacencia = {node: set() for node in self.no}
        for aresta in arestas:
            self.lista_de_adjacencia[aresta[0]].add((aresta[1], aresta[2]))

    def menor_caminho(self, no_comeco, no_final):
        

        nos_nao_visitados = self.no.copy()

     
        distancia_do_comeco = {
            node: (0 if node == no_comeco else INFINITO) for node in self.no
        }

       
        no_anterior = {node: None for node in self.no}

        while nos_nao_visitados:
           
            no_atual = min(
                nos_nao_visitados, key=lambda node: distancia_do_comeco[node]
            )
            nos_nao_visitados.remove(no_atual)

           
            if distancia_do_comeco[no_atual] == INFINITO:
                break

            
            for vizinhanca, distance in self.lista_de_adjacencia[no_atual]:
                novo_caminho = distancia_do_comeco[no_atual] + distance
                if novo_caminho < distancia_do_comeco[vizinhanca]:
                    distancia_do_comeco[vizinhanca] = novo_caminho
                    no_anterior[vizinhanca] = no_atual

            if no_atual == no_final:
                break 

      
        caminho = deque()
        no_atual = no_final
        while no_anterior[no_atual] is not None:
            caminho.appendleft(no_atual)
            no_atual = no_anterior[no_atual]
        caminho.appendleft(no_comeco)

        return caminho, distancia_do_comeco[no_final]


def main():
  
 
    no_de_entrada = input('Nó Start: ')
    no_de_chegada = input('Nó End: ')
    graph = meu_grafo('dados.txt')
    menorcaminho, menordistancia = graph.menor_caminho(no_de_entrada,no_de_chegada)
    if menordistancia == INFINITO:
        print("Não existe caminho possível")
    else:
        print("Menor caminho: ", end="")
        print(*menorcaminho)
        print(f"Menor distância: {menordistancia}")



if __name__ == "__main__":
    main()
