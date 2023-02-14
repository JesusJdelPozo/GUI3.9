import numpy as np
from itertools import combinations


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

def get_new_guess(guesses, scores):
    if len(guesses) == 0:
        return np.random.choice(range(10), 5, replace=False)
    else:
        num_rigth = [score[0] + score[1] for score in scores]
        # best_guess =1



def main():
    secret_number = np.random.choice(range(10), 5, replace=False)
    print(secret_number)
    print('Esto es Toque y Fama teclea un número de 5 dígitos distintos')
    guesses = []
    scores = []

    while len(guesses) < 10:
        # digits = ask_input()
        digits = np.random.choice(range(10), 5, replace=False)
        print(digits)
        guesses.append(digits)
        score = get_tokes_famas(digits, secret_number)
        print(score)
        scores.append(score)
        print(scores)
        if score[1] == 5:
            print('Ese es el número secreto')
            print('Felicidades as ganado!')
            break
        else:
            print(f'tienes {score[0]} tokes y {score[1]} famas')
            print('Escribe otro número')
    for i, guess in enumerate(guesses):
        print(guess)
        print(scores[i])



if __name__=='__main__':
    main()