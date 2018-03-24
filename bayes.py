import math
from scrapper import split

class NaiveBayesClassifier:

    def __init__(self, alpha = 1):
        self.alpha = alpha

    def fit(self, X, y): # x=title; y = label
        """ Fit Naive Bayes classifier according to X, y. """
        self.labels = [
            for i in set(y)
        ]
        self.labels.sort()
        massive_from_lables = 0 * len(self.labels)
        for i in range(len(y)):
            y[i] = self.labels.index(y[i])+1
            massive_from_labels[y[i] - 1] += 1
        self.word_index = [[] for i in range(len(self.labels) * 2 + 1)]
        self.formula_bayes = [math.log(l/ sum(massive_from_lables) for l in massive_from_labels)]
        for i in range(len(X)):
            word = split(X[i])
            for w in word :
                if w not in self.word_index:
                    self.word_index[0].append(w)
                    self.word_index[y[i]].append(1)
                    for lab in range(len(self.labels) -1) :
                        y[i] = (y[i]% len(self.labels)) + 1
                        self.word_index[y[i]].append(0)
                    for col in range(len(self.labels)+1, len(self.labels)*2 + 1):
                        self.word_index[col].append(0)
                else:
                    self.word_index[y[i]][self.word_index[0].index(w)] +=1
        word_with_lab = [sum(self.word_index[i +1]) for i in range(len(self.labels))]

        for row in range(len(self.word_index[0])):
            for col in range(len(self.labels) + 1, len(self.labels) * 2 + 1):
                self.word_index[row][col] = (self.word_index[col - len(self.labels) ][row] + self.alpha) / \ (word_with_lab[col - len(self.labels) - 1] + self.alpha * len (self.word_index[0]))






    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        lables = []
        for p in X:
            str_lab  = [for i in self.formula_bayes]
            word = split(p)
            for w in word:
                if w in self.word_index[0]:
                    for i in range(len(self.lables)):
                        str_lab[i] += math.log(self.word_index[i + len(self.lables + 1)][self.word_index[0].index(w)])
            for i in range(len(self.labels)):
                if str_lab == max(str_lab):
                    lables.append(self.labels[i])
                    break
        return lables


    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        cnt = 0
        for i in range(len(self.formula_bayes(X_test))):
            if self.formula_bayes[i] == y_test[i]:
                cnt += 1
        score = cnt / len(y_test)
        return score


