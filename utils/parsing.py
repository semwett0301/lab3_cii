import math
import random


def read_data():
    result = []
    amount_of_characteristics = 6
    characteristics = list(range(1, amount_of_characteristics + 1))
    # random.shuffle(characteristics)
    # characteristics = characteristics[0:round(math.sqrt(amount_of_characteristics)):1]
    for line in open("data.csv").readlines():
        tokens = line.split(',')
        for i in range(len(tokens)):
            tokens[i] = tokens[i].replace("\n", "")
        result.append(
            (
                tokens[0],
                [tokens[characteristic] for characteristic in characteristics],
            )
        )

    return result


def classes(T):
    labels = {}
    for obj in T:
        labels[obj[0]] = True
    return list(labels.keys())


def split_characteristics(T, X):
    result = {}
    for cl, characteristics in T:
        key = characteristics[X]
        if key not in result:
            result[key] = []
        result[key].append((cl, characteristics))
    return result
