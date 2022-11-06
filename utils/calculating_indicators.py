def calculate_indicators(answers, positive):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for prediction, fact in answers:
        if prediction == fact:
            if fact == positive:
                tp += 1
            else:
                tn += 1
        else:
            if fact == positive:
                fp += 1
            else:
                fn += 1

    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    return accuracy, precision, recall
