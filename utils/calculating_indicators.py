def calculate_indicators(answers, classes):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for prediction, fact in answers:
        if prediction == fact:
            if fact == classes[0]:
                tp += 1
            else:
                tn += 1
        else:
            if fact == classes[0]:
                fp += 1
            else:
                fn += 1

    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    return accuracy, precision, recall
