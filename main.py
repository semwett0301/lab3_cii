from utils.calculating_indicators import calculate_indicators
from utils.tree import make_prediction
from utils.parsing import read_data
from utils.tree import build_tree

data = read_data()
tree = build_tree(data)

answers = []
classes = []
for cl, characteristics in data:
    if cl not in classes:
        classes.append(cl)
    prediction = make_prediction(characteristics, tree)
    print(f'Predicted: {prediction}, Real: {cl}')
    answers.append((prediction, cl))
accuracy, precision, recall = calculate_indicators(answers, classes)

print()
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
