import numpy as np
from itertools import permutations


def ask_input():
    while True:
        number = input()
        if valid_input(number):
            digits = [int(d) for d in number]
            digits = np.array(digits)
            break
    return digits


def valid_input(number) -> bool:
    try:
        digits = [int(d) for d in number]
        l = len(digits)
        if l != 5 or len(set(digits)) != l:
            print('Ese no es un número con 5 dígitos distintos!!')
            print('Intentalo de nuevo')
            return False
        else:
            return True
    except ValueError:
        digits = []
        print('Eso no es un número!')
        print('Inténtalo de nuevo')
        return False


def get_tokes_famas(digits, secret):
    ntokes = 0
    nfamas = 0
    for i, d in enumerate(digits):
        for j, s in enumerate(secret):
            if s == d:
                if i == j:
                    nfamas += 1
                else:
                    ntokes += 1
    return ntokes, nfamas

def pick(slots):
    digits = np.ones(5, dtype=int) * 10
    pos = [int(p) for p in range(10)]
    aux = []
    for i in range(5):
        while not aux:
            aux = [int(p) for p in pos if i in slots[p][:]]
        num = np.random.choice(aux, 1)
        pos.remove(num)
        digits[i] = num
        aux = []

    return digits

def sieve(guesses, scores, slots):
    score = scores[-1]
    digits = guesses[-1]
    if score[1] == 0:
        for i, d in enumerate(digits):
            slots[d].remove(i)
    elif score[0] + score[1] == 0:
        for d in digits:
            slots[d] = []
    elif score[0] + score[1] == 5:
        digits2 = [d for d in range(10) if d not in digits]
        for i, d in enumerate(digits2):
            slots[d] = []

def main():
    secret_number = np.random.choice(range(10), 5, replace=False)
    print(secret_number)
    print('Esto es Toque y Fama teclea un número de 5 dígitos distintos')
    guesses = []
    scores = []
    slots = [[0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4]]

    for counter in range(1000):
        digits = pick(slots)
        print(digits)
        guesses.append(digits)
        score = get_tokes_famas(digits, secret_number)
        scores.append(score)
        sieve(guesses, scores, slots)
        print(counter)
        if score[1] == 5:
            print('Ese es el número secreto')
            print('Felicidades as ganado!')

            return 1
        else:
            print(f'tienes {score[0]} tokes y {score[1]} famas')
            print('Escribe otro número')
        # a = input('press a key to continue')
    print(secret_number)
    # print(slots)
    # print(guesses)


if __name__=='__main__':
    c = 0
    trials = 10000
    for i in range(trials):
        c += main()
        print(c)

    print(f'Funciono {c} veces de {trials} intentos')