import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class GDRegressor:
    def __init__(self, alpha=0.000001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta_history = [0] * self.max_iter  # переменная для сохранения теты
        self.cost_history = [0] * self.max_iter  #  переменная для сохранения значений целевой функции

    def fit(self, X_train, y_train): # добавить столбец из единичек в нулевую матрицу х

        """
        Обучаем модель на данных
        :param X_train: матрица признаков
        :param y_train: матрица ответов
        :return: coef_ - вектор оценок для theta_i (i - значение от 1 до p, p - количество признаков),
        intercept_ - оценённое значение для theta_0
        """
        X = X_train.copy()
        X.insert(0, "Ones", np.ones(len(X)))
        self.theta = np.zeros(X.shape)  # создаём нулевую матрицу для значений теты, рамзером с выборку
        t = X.T
        m = len(y)
        for i in range(1, self.max_iter):
            """
            цикл, внутри которого будем высчитывать значения теты, сохранять значения целевой функции
            """
            # формула градиентного спуска, для подсчёта значений теты
            self.theta -= self.alpha * 1 / m * (t.dot(X.dot(self.theta.reshape((2, m)) - y_train))).as_matrix().reshape((m, 2))
            #x.dot(theta) - y ;
            # записываем старые значения теты
            self.theta_history[i] = self.theta
            # записываем старые значения целевой функции
            self.cost_history[i] = sum((self.theta * X.as_matrix() - y.reshape((40, 2)) ** 2)) / (2 * m)

        self.coef_ = self.theta[1]
        self.intercept_ = self.theta[0]

        return self.coef_, self.intercept_

    def predict(self, X_test):
        """
        :param X_test: тестовая выборка
        :return: вектор прогнозов для новых данных (произведение тестовой выборки на вектор весов)
        """
        X = X_test.copy()
        X.insert(0, "Ones", np.ones(len(X)))
        m = X_test.size  # считаем размер выборки
        y = X.dot(self.theta.reshape(2, m))  # перемножаем выборку и вектор весов
        self.pred = y[0]

        return self.pred


if __name__ == '__main__':
    df = pd.read_csv('brain_size.csv')
    X = df.iloc[:, 1:2]
    Y = df.iloc[:, 2:3]
    model = GDRegressor()
    model.fit(X, Y)
    model.predict(X)
    #df.plot(kind='scatter', x="FSIQ", y="VIQ")
    #plt.plot(X, model.coef_[0] * X + model.intercept_, 'r')
    plt.plot(range(len(model.cost_history) - 1), [model.cost_history[i][0] for i in range(1, len(model.cost_history)) for j in range(1)])
    plt.show()
