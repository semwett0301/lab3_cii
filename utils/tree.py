from utils.parsing import classes, split_characteristics
from utils.rating import calculate_best_x


def build_tree(T):
    current_best_X = calculate_best_x(T)
    current_result = split_characteristics(T, current_best_X)
    if len(current_result.keys()) == 1:
        return classes(T)[0]
    return {current_best_X: {key: build_tree(current_result[key]) for key in current_result.keys()}}


def make_prediction(characteristics, tree):
    current_characteristic = list(tree.keys())[0]
    decision = tree[current_characteristic][characteristics[current_characteristic]]
    return decision if type(decision) == str else make_prediction(characteristics, decision)
