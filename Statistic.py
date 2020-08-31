import numpy as np
import pandas as pd

class Statistic:
    def __init__(self):
        self.value_inf = [30, 35, 40, 45, 50]
        self.value_sup = [35, 40, 45, 50, 55]
        self.value_class = [f"{self.value_inf[i]}|--{self.value_sup[i]} " for i in range(0, len(self.value_inf))]
        self.xi = [(self.value_inf[i] + self.value_sup[i])/2 for i in range(0, len(self.value_inf)) ]
        self.fi = [7, 12, 20, 16, 5]
        self.fixi = [self.xi[i]*self.fi[i] for i in range(0, len(self.xi))]
        self.far = self.weighted_sum(self.fi)[0]
        self.wi = [i - self.xi[0] for i in self.xi]
        self.wi_sqrt = [i*i for i in self.wi]
        self.fiwi = [self.fi[i]*self.wi[i] for i in range(0, len(self.xi))]
        self.fiwi_sqrt = [self.fi[i]*self.wi_sqrt[i] for i in range(0, len(self.xi))]
        self.fr = [i/self.far[1] for i in self.fi]
        self.frac = self.weighted_sum(self.fr)[0]
        self.table = {"Classe": self.value_class,
                      "xi": self.xi,
                      "fi": self.fi,
                      "fixi": self.fixi,
                      "Fac": self.far,
                      "wi": self.wi,
                      "wi²": self.wi_sqrt,
                      "fiwi": self.fiwi,
                      "fiwi²": self.fiwi_sqrt,
                      "fr": self.fr,
                      "frac": self.frac}

        self.summation = {"Σ(xi)": self.weighted_sum(self.xi)[1],
                          "Σ(fi)": self.weighted_sum(self.fi)[1],
                          "Σ(fixi)": self.weighted_sum(self.fixi)[1],
                          "Fac": None,
                          "Σ(wi)": self.weighted_sum(self.wi)[1],
                          "Σ(wi²)": self.weighted_sum(self.wi_sqrt)[1],
                          "Σ(fiwi)": self.weighted_sum(self.fiwi)[1],
                          "Σ(fiwi²)": self.weighted_sum(self.fiwi_sqrt)[1],
                          "Σ(fr)": self.weighted_sum(self.fr)[1],
                          "frac": None}

        self.df = pd.DataFrame(self.table)
        self.df_00 = pd.DataFrame(self.summation, index=[0])
        print(self.df)
        print(self.df_00)

    def generator(self):
        for i in range(0, 5):
            value = float(input(f"Digite o valor do X {str(len(self.xi))}: "))
            frequency = float(input(f"Digite a frequência de {value}: "))
            assert isinstance(value, int) or isinstance(value, float)
            assert isinstance(frequency, int) or isinstance(frequency, float)
            self.xi.append(value)
            self.fi.append(frequency)

    @staticmethod
    def weighted_sum(value):
        assert isinstance(value, tuple) or isinstance(value, list)
        vector = list()
        sum = 0
        for i in value:
            sum = sum + i
            vector.append(sum)
        return [vector, sum]

    def data_average(self):
        return self.summation["Σ(fixi)"]/self.summation["Σ(fi)"]

    def moda(self):
        pass

    def generator_csv(self):
        pass




if __name__ == '__main__':
    objeto = Statistic()
    objeto.generator_csv()
    print('Média: ', objeto.data_average())
