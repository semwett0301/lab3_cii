import math

from utils.parsing import classes, split_characteristics


def freq(label, data):
    return len(list(filter(lambda item: item[0] == label, data)))


def info(T):
    return -sum([freq(C, T) / len(T) * math.log2(freq(C, T) / len(T)) for C in classes(T)])


def info_x(T, X):
    return sum([len(T_i) / len(T) * info(T_i) for T_i in split_characteristics(T, X).values()])


def split_info_x(T, X):
    return -sum([len(Ti) / len(T) * math.log2(len(Ti) / len(T)) for Ti in split_characteristics(T, X).values()])


def gain_ratio(T, X):
    sx = split_info_x(T, X)
    if sx == 0:
        return None
    return (info(T) - info_x(T, X)) / sx


def calculate_best_x(T):
    best_X = 0
    cl, characteristic = T[0]
    for X in range(len(characteristic)):
        current_gain = gain_ratio(T, X)
        best_gain = gain_ratio(T, best_X)
        if not(current_gain is None) and not(best_gain is None) and current_gain > best_gain:
            best_X = X
    return best_X
