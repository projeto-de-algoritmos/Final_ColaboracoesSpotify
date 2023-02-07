# Final_ColaboracoesSpotify

**Número da Lista**: 9<br>
**Conteúdo da Disciplina**: Trabalho Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0141842  |  Philipe Rosa Serafim |
| 16/0143403  |  Renan Welz Schadt |

## Sobre 
O objetivo do trabalho foi por em prática os conceitos aprendidos durante a disciplina de Projeto de Algoritimos, onde foram implementados diferentes algoritmos para encontrar o menor caminho entre dois nós dentro do grafo construído.

A equipe utilizou duas base de dados do Spotify disponíveis no Kaggle, filtrou e reuniu informações das duas.

A primeira base contém músicas e os artistas responsáveis por elas, fizemos um filtro para pegar apenas as músicas com mais de 1.2 milhões de streams e lançadas entre os anos de 2010 e 2020 na plataforma Spotify. A segunda base contém artistas e seu nível de popularidade (0 a 100) que é definido de acordo com quantos seguidores esse artista possui no Spotify. Tendo posse das músicas, artistas e níveis de popularidade no formato que foi definido pela dupla, foi iniciada a implementação da estrutura do grafo.

O grafo é contruído de forma que os artistas são os nós, as arestas são as colaborações entre os artistas (feats) e o peso das arestas é a popularidade somada dos artistas conectados pela aresta. De modo a priorizar o caminho com artistas populares a escala de popularidade foi invertida, de forma que o artista mais popular tem popularidade 1 e o menos tem popularidade 100.

A estrutura dos grafos foi implementada de três formas distintas e foram usados três diferentes algoritmos para encontrar o menor caminho.

* O grafo foi implementado através de uma lista de adjascências em que foi usado o BFS para encontrar os 3 menores caminhos, sendo esses definidos pelo menor número de arestas percorridas sem contar o peso.
* O grafo foi implementado através de uma lista de arestas em que foi usado o Djkstra para encontrar o menor caminho, sendo que o menor caminho considera os pesos das arestas.
* O grafo foi implementado através de uma biblioteca específica do Python para utilização de grafos chamada networkX em que foi usado o Bellman-Ford para encontrar o menor caminho, sendo que o menor caminho considera os pesos das arestas. Bellman-Ford também foi utilizado para determinar o tamanho da nuvem onde o nó está conectado.


Por último, foi utilizado a implementação de grafos de uma biblioteca externa, a NetworkX, para que fosse possível ilustrar os resultados obtidos com o algoritmo implementado.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python<br>

 - Instalar e configurar o Python3/Pip3
 - Primeiro deve-se clonar o repositório
 - Tendo clonado o repositório deve-se entrar na pasta do projeto e então rodar o comando `pip install -r requirements.txt`.
 O pip install irá instalar todas as bibliotecas necessárias para rodar o projeto, caso isso não ocorra como esperado, deve-se instalar manualmente.

## Uso 
- Após a instalação das bibliotecas, entrar na pasta src e executar o arquivo main.py da seguinte forma: `python3 main.py`.





