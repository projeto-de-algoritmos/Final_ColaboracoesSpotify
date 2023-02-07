# -*- coding: utf-8 -*-

import difflib as dl
import time
import networkxGraph

def correct_input(min_value, max_value):
    while True:
        try:
            option = int(input('Escolha uma das opções acima \n'))
            if option >= min_value and option <= max_value:
                return option
            else:
                print(f'Digite um número entre {min_value} e {max_value}')
        except:
            print('Opção inválida. Digite um número')

def choose_artist(artistPos, g):
    artistName = input(f'Digite o nome do {artistPos} artista \n')
    closestMatches = dl.get_close_matches(artistName, g.translateNodes)

    print("\nForam encontrados os seguintes artistas a partir da sua pesquisa, qual deseja selecionar?")
    for i, artist in enumerate(closestMatches):
        print(f"{i} - {artist}")

    artistOption = correct_input(0, len(closestMatches)-1)
    print()
    return closestMatches[artistOption]

def printPath(final_artists, final_songs, multiple):
    print()
    print("Caminhos no formato Artista -> Musica -> Artista -> Musica ... \n")

    if multiple == True:
        for i, songsList in enumerate(final_songs):
            print(f"Caminho {i+1}:")
            for j, songs in enumerate(songsList):
                print(f"{final_artists[i][j]} -> {final_songs[i][j]} ->", end=" ")
            print(f"{final_artists[i][len(songsList)]}")

            print('\n\n')
    else:
        for j, songs in enumerate(final_songs):
            print(f"{final_artists[j]} -> {final_songs[j]} ->", end=" ")
        
        print(f"{final_artists[len(final_songs)]}")
        print('\n\n')


def get_songs(g, artistList):
    songList = []
    for i, artist in enumerate(artistList[:-1]):
        for collaboration in g.graph[artist]:
            if collaboration[0] == artistList[i+1]:
                songList.append(collaboration[1])
    
    return songList

def menu(g, networkXG, edgeListG):
    print("Spotify Colaborações Musicais.")
    
    while True:
        print("1 - Encontre o menor caminho de músicas que liga dois artistas usando BFS.")
        print("2 - Encontre o menor caminho de músicas que liga dois artistas usando Djkstra.")
        print("3 - Encontre o menor caminho de músicas que liga dois artistas usando BellmanFord.")
        print("4 - Encontre o número de artistas acessíveis a partir de outro artista com BellmanFord.")
        print("5 - Finalizar programa.\n")
        
        action = correct_input(1, 5)
        
        if action == 1:
            artist1 = choose_artist('primeiro', g)
            artist2 = choose_artist('segundo', g)

            artistList, songList = g.BFS_shortest_path(artist1, artist2)
            if artistList != []:
                printPath(artistList, songList, True)
            else:
                print("Não existe caminho entre os dois artistas.\n")

        elif action == 2:
            artist1 = choose_artist('primeiro', g)
            artist2 = choose_artist('segundo', g)

            dist, artistList = edgeListG.djsktraShortestPath(artist1, artist2)
            if artistList != []:
                songList = get_songs(g, artistList)
                print("Distância: ", dist)
                printPath(artistList, songList, False)
            else:
                print("Não existe caminho entre os dois artistas.\n")
        
        elif action == 3:
            artist1 = choose_artist('primeiro', g)
            artist2 = choose_artist('segundo', g)
            
            artistList = networkxGraph.shortest_path(networkXG, artist1, artist2)
            dist = networkxGraph.shortest_dist(networkXG, artist1, artist2)
            
            if artistList != []:
                songList = get_songs(g, artistList)
                print("Distância: ", dist)
                printPath(artistList, songList, False)
            else:
                print("Não existe caminho entre os dois artistas.\n")

        elif action == 4:
            artist1 = choose_artist('primeiro', g)
            connectedArtists = networkxGraph.acessible_nodes(networkXG, artist1)

            print(f"\nA nuvem onde o artista {artist1} está conectado contém {str(connectedArtists)} elementos. Todos são acessíveis a partir de {artist1}\n")
        
        else:
            return

        
        time.sleep(2)

