import numpy as np


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


def pick(slots, guesses, scores):
    if guesses:
        digits = np.ones(5, dtype=int) * 10
        while True:
            digits = [int(np.random.choice(a, 1)) for a in slots]
            if len(digits) == len(set(digits)):
                break
    else:
        digits = np.random.choice(range(10), 5, replace=False)

    return digits


def sieve(guesses, scores, slots):
    score = scores[-1]
    digits = guesses[-1]
    undertermined = [k for k in range(5) if len(slots[k]) > 1]

    if score[1] == 5 - len(undertermined):
        [slots[i].remove(digits[i]) for i in undertermined]

    elif score[0] + score[1] == 0:
        for d in digits:
            [slots[k].remove(d) for k in range(5) if d in slots[k]]

    elif score[0] + score[1] == 5:
        digits2 = [d for d in range(10) if d not in digits]
        for d in digits2:
            [slots[k].remove(d) for k in range(5) if d in slots[k]]

    num = [slots[i] for i in range(5) if len(slots[i]) == 1]
    for d in num:
        [slots[k].remove(d) for k in range(5) if d in slots[k] and len(slots[k]) > 1]

    flag = True
    while flag:
        flag = False
        undertermined = [k for k in range(5) if len(slots[k]) > 1]
        for guess, score in zip(guesses, scores):
            posible_famas = [j for j in undertermined if guess[j] in slots[j]]
            if len(posible_famas) == score[1] - (5 - len(undertermined)):
                for fama in posible_famas:
                    [slots[m].remove(guess[fama]) for m in undertermined if guess[fama] in slots[m]]
                    slots[fama] = [guess[fama]]
                    flag = True

    return slots


def main():
    secret_number = np.random.choice(range(10), 5, replace=False)
    # print(secret_number)
    # print('Esto es Toque y Fama teclea un número de 5 dígitos distintos')
    guesses = []
    scores = []
    slots = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

    for counter in range(1000):
        digits = pick(slots, guesses, scores)
        # print(digits, slots)
        guesses.append(digits)
        score = get_tokes_famas(digits, secret_number)
        scores.append(score)
        slots = sieve(guesses, scores, slots)
        # print(counter)
        if score[1] == 5:
            # print('Ese es el número secreto')
            # print('Felicidades as ganado!')

            return counter
        # else:
        #     # print(f'tienes {score[0]} tokes y {score[1]} famas')
        #     # print('Escribe otro número')
    #     # a = input('press a key to continue')


if __name__ == '__main__':
    c = 0
    trials = 10
    for i in range(trials):
        c += main()
        # print(i, c)

    print(f'Funciono {c / 10000} veces de {trials} intentos')
