import matplotlib.pyplot as plt

from utils.calculating_indicators import calculate_indicators


def draw_auc_roc(answers):
    answers.sort(key=lambda item: item[0] == 'POISONOUS')

    x = [0]
    y = [0]
    for i in range(0, len(answers)):
        if answers[i][1] == answers[i][0]:
            x.append(x[-1])
            y.append(y[-1] + 0.0001)
        else:
            x.append(x[-1] + 0.0001)
            y.append(y[-1])
    plt.plot(x, y)
    plt.title("AUC-ROC")
    plt.show()


def draw_auc_pr(answers, positive):
    answers.sort(key=lambda item: item[0] == 'EDIBLE')

    x = [0]
    y = [1]
    for i in range(0, len(answers)):
        if answers[i][1] != answers[i][0]:
            if answers[i][0] == 'EDIBLE':
                x.append(x[-1])
                y.append(y[-1] - 0.0001)
            else:
                x.append(x[-1] + 0.0001)
                y.append(y[-1])
    plt.plot(x, y)
    plt.title("AUC-PR")
    plt.show()

