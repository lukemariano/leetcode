from itertools import permutations


def getPermutation(n: int, k: int) -> str:
    # Cria uma lista ordenada com range de n
    permutation_list = [*range(1, n + 1)]
    # gera permutações com a permutation_list
    permuts = permutations(permutation_list)

    perm_tupla = None
    contador = 1

    # Verifica a posição correta da permutação para 'k'
    for perm in permuts:
        if contador == k:  # se perm for igual a permutação na posição 'k' --> break
            perm_tupla = perm  # salva a permutação em uma variável
            break
        contador += 1

    # Converte a tupla para string
    resultado = ""
    for n in perm_tupla:
        resultado += str(n)

    return resultado  # output


print(getPermutation(n=3, k=3))
