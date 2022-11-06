from utils.calculating_indicators import calculate_indicators
from utils.tree import make_prediction
from utils.parsing import read_data
from utils.tree import build_tree
from utils.drawing import draw_auc_roc, draw_auc_pr

data = read_data()
tree = build_tree(data)

answers = []
positive = 'EDIBLE'

for cl, characteristics in data:
    prediction = make_prediction(characteristics, tree)
    print(f'Predicted: {prediction}, Real: {cl}')
    answers.append((prediction, cl))
accuracy, precision, recall = calculate_indicators(answers, positive)

print()
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')

draw_auc_roc(answers)
draw_auc_pr(answers, positive)


