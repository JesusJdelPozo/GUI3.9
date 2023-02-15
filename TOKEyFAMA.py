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

def get_new_guess(guesses, scores):
    if len(guesses) == 0:
        return np.random.choice(range(10), 5, replace=False)
    else:
        num_rigth = [score[0] + score[1] for score in scores]
        # best_guess =1

def pick(posible, slots):
    digits = np.ones(5, dtype=int) * 10
    print(digits, posible, slots[1][1])
    length = [len(slots[n]) for n in posible]
    len_sorted = np.argsort(length)
    print(len_sorted[-1:-6:-1])
    numbers = [posible[i] for i in len_sorted[-1:-6:-1]]
    print(numbers)
    pos = []
    while len(pos) != 5:
        positions = [int(np.random.choice(slots[n][:], 1)) for n in numbers]
        print(positions)
        pos = list(set(positions))

    for i in range(5):
        print(positions[i], numbers[i])
        digits[positions[i]] = int(numbers[i])

    return digits


def main():
    secret_number = np.random.choice(range(10), 5, replace=False)
    print(secret_number)
    print('Esto es Toque y Fama teclea un número de 5 dígitos distintos')
    guesses = []
    scores = []
    posible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    digits = pick(posible, slots)
    print(digits)

    digits1 = [0, 1, 2, 3, 4]
    digits2 = [5, 6, 7, 8, 9]
    for counter in range(5):
        # digits = ask_input()
        # print(digits)
        if np.mod(counter, 2) == 0:
            digits = digits1
        else:
            digits = digits2
        guesses.append(digits)
        score = get_tokes_famas(digits, secret_number)
        scores.append(score)
        # print(guesses)
        for d in digits:
            totalmap[d, 0] += score[0]
            totalmap[d, 1] += score[1]
        if np.mod(counter, 2) == 1:
            toke_ordering = np.argsort(totalmap[:, 0])
            # print(toke_ordering)
            cnt = 0
            flag = True
            flag2 = True
            while flag:
                if flag2:
                    digits1 = toke_ordering[::2]
                    flag2 = False
                else:
                    digits1 = toke_ordering[cnt:cnt+5]
                    flag2 = True

                if cnt > 0:
                    np.random.shuffle(digits1)

                check = [digits1 == g for g in guesses]
                f =np.array([c.all() == True for c in check])
                flag = f.any() == True
                cnt += 1

            digits1 = list(digits1)
            digits2 = [t for t in toke_ordering if t not in digits1]
            if len(digits2) < 5:
                print('warning', digits1, digits2)
                digits2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                for d in digits1:
                    digits2.remove(d)
                print(digits2)



        print(counter)
        if score[1] == 5:
            print('Ese es el número secreto')
            print('Felicidades as ganado!')

            break
        # else:
        #     print(f'tienes {score[0]} tokes y {score[1]} famas')
        #     print('Escribe otro número')
        # a = input('press a key to continue')
    # for i, guess in enumerate(guesses):[1 2 6 5 8]
    #     tokes[scores[i][0]] += 1
    #     famas[scores[i][1]] += 1
    #     tokefama[scores[i][0], scores[i][1]] += 1
    #     for j, d in enumerate(guess):
    #         tmap[d, j] += scores[i][0]
    #         fmap[d, j] += scores[i][1]
    #         totalmap[d] += scores[i][0]+scores[i][1]
    #
    # print(tokes)
    # print(famas)
    # print(tokefama)
    # print(tmap)
    # print(fmap)
    # print(totalmap)
    # print(len(guesses))

# [ 1546.  7300. 12460.  7520.  1370.    44.]
# [1.8089e+04 9.5450e+03 2.2700e+03 3.1000e+02 2.5000e+01 1.0000e+00]
# [[1.200e+02 6.000e+02 6.000e+02 2.000e+02 2.500e+01 1.000e+00]
#  [2.400e+03 3.600e+03 1.200e+03 1.000e+02 0.000e+00 0.000e+00]
# [7.800e+03 4.200e+03 4.500e+02 1.000e+01 0.000e+00 0.000e+00]
# [6.400e+03 1.100e+03 2.000e+01 0.000e+00 0.000e+00 0.000e+00]
# [1.325e+03 4.500e+01 0.000e+00 0.000e+00 0.000e+00 0.000e+00]
# [4.400e+01 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00]]

if __name__=='__main__':
    main()