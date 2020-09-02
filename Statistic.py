import numpy as np
import pandas as pd
import math


# gerente - > modulos com partes da estatistica

class Statistic:
    def __init__(self, chave):
        self.value_inf = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5]
        self.value_sup = [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
        self.value_class = [f"{self.value_inf[i]}|--{self.value_sup[i]} " for i in range(0, len(self.value_inf))]

        self.xi = [(self.value_inf[i] + self.value_sup[i]) / 2 for i in range(0, len(self.value_inf))]
        self.xi_sqrt = [i * i for i in self.xi]

        if chave == 0:
            self.yi = [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
            self.yi_sqrt = [i * i for i in self.yi]
            self.xiyi = [self.xi[i] * self.yi[i] for i in range(0, len(self.xi))]

        self.fi = [7, 13, 19, 24, 15, 2]
        self.fixi = [self.xi[i] * self.fi[i] for i in range(0, len(self.xi))]
        self.far = self.weighted_sum(self.fi)[0]
        self.wi = [i - self.xi[0] for i in self.xi]
        self.wi_sqrt = [i * i for i in self.wi]
        self.fiwi = [self.fi[i] * self.wi[i] for i in range(0, len(self.xi))]
        self.fiwi_sqrt = [self.fi[i] * self.wi_sqrt[i] for i in range(0, len(self.xi))]
        self.fr = [i / self.far[1] for i in self.fi]
        self.frac = self.weighted_sum(self.fr)[0]

    def generator(self, chave):
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
        return self.summation["Σ(fixi)"] / self.summation["Σ(fi)"]

    def mode(self):
        ind_mo = np.argmax(self.table['fi'])
        f_sup = self.table["fi"][ind_mo + 1]
        f_inf = self.table["fi"][ind_mo - 1]
        h = self.value_sup[ind_mo] - self.value_inf[ind_mo]
        return self.value_inf[ind_mo] + (f_sup / (f_sup + f_inf)) * h

    #
    def median(self):
        N = self.summation["Σ(fi)"] / 2
        for index, value in enumerate(self.table['Fac']):
            if value >= N:
                intervalo_mediana = index
                break
        limit_inf = self.table['Fac'][intervalo_mediana - 1]
        fi = self.table['fi'][intervalo_mediana]
        h = self.value_sup[intervalo_mediana] - self.value_inf[intervalo_mediana]
        return self.value_inf[intervalo_mediana] + ((N - limit_inf) / fi) * h

    #
    def quartis(self):
        vector = [1 / 4, 2 / 4, 3 / 4]
        quartis = []
        for i in vector:
            N = self.summation["Σ(fi)"] * i
            for index, value in enumerate(self.table['Fac']):
                if value >= N:
                    intervalo_mediana = index
                    break
            if intervalo_mediana >= 1:
                limit_inf = self.table['Fac'][intervalo_mediana - 1]
            else:
                limit_inf = 0
            fi = self.table['fi'][intervalo_mediana]
            h = self.value_sup[intervalo_mediana] - self.value_inf[intervalo_mediana]
            quartis.append(self.value_inf[intervalo_mediana] + ((N - limit_inf) / fi) * h)
        return quartis

    #
    def percentis(self):
        a = [1 / 10, 2 / 10, 3 / 10, 4 / 10, 5 / 10, 6 / 10, 7 / 10, 8 / 10, 90 / 100]
        percentis = []
        for i in a:
            N = self.summation["Σ(fi)"] * i
            for index, value in enumerate(self.table['Fac']):
                if value >= N:
                    intervalo_mediana = index
                    break
            # try exeption 0
            if intervalo_mediana >= 1:
                limit_inf = self.table['Fac'][intervalo_mediana - 1]
            else:
                limit_inf = 0
            fi = self.table['fi'][intervalo_mediana]
            h = self.value_sup[intervalo_mediana] - self.value_inf[intervalo_mediana]
            percentis.append(self.value_inf[intervalo_mediana] + ((N - limit_inf) / fi) * h)
        return percentis

    def tables(self, number_table=1):
        if number_table == 0:
            self.table = {"Classe": self.value_class,
                          "xi": self.xi,
                          "fi": self.fi,
                          "fixi": self.fixi,
                          "Fac": self.far,
                          "fr": self.fr,
                          "frac": self.frac}

            self.summation = {"Index": "Value",
                              "Σ(xi)": self.weighted_sum(self.xi)[1],
                              "Σ(fi)": self.weighted_sum(self.fi)[1],
                              "Σ(fixi)": self.weighted_sum(self.fixi)[1],
                              "Fac": None,
                              "Σ(fr)": self.weighted_sum(self.fr)[1],
                              "frac": None}

            self.df = pd.DataFrame(self.table)
            self.df_00 = pd.DataFrame(self.summation, index=[0])
            print(self.df)
            print(self.df_00)

        elif number_table == 1:
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

            self.summation = {"Index": "Value",
                              "Σ(xi)": self.weighted_sum(self.xi)[1],
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

        elif number_table == 2:
            self.table = {"Classe": self.value_class,
                          "xi": self.xi,
                          "yi": self.yi,
                          "xi²": self.xi_sqrt,
                          "yi²": self.yi_sqrt,
                          "xiyi": self.xiyi}

            self.summation = {"Index": "Value",
                              "Σ(xi)": self.weighted_sum(self.xi)[1],
                              "Σ(yi)": self.weighted_sum(self.fi)[1],
                              "Σ(xi²)": self.weighted_sum(self.xi_sqrt)[1],
                              "Σ(yi²)": self.weighted_sum(self.yi_sqrt)[1],
                              "Σ(xiyi)": self.weighted_sum(self.xiyi)[1]}

        self.df = pd.DataFrame(self.table)
        self.df_00 = pd.DataFrame(self.summation, index=[0])
        print(self.df)
        print(self.df_00)

    def generator_csv(self):
        pass

    def variance(self, vector):
        vector_01 = [i * i for i in vector]
        n = len(vector)
        a = 1 / (n - 1)
        return (self.weighted_sum(vector_01)[1] - (1 / n) * (self.weighted_sum(vector)[1] ** 2))

    def variance_pearson(self, vector):
        vector_01 = [i * i for i in vector]
        n = len(vector)
        a = 1 / (n - 1)
        return (1 / n - 1) * (self.weighted_sum(vector_01)[1] - (1 / n) * (self.weighted_sum(vector)[1] ** 2))

    def r_pearson(self):
        pass

    def standard_deviation(self, variance):
        return math.pow(variance, 1 / 2)

    def covariance(self, vector_x, vector_y):
        pass


if __name__ == '__main__':
    objeto = Statistic(0)
    objeto.tables(2)
    print(f"variance: {objeto.variance(objeto.xi)}")
    print(f"variance: {objeto.variance_pearson(objeto.xi)}")
    print(f"variance: {objeto.variance(objeto.yi)}")
    print(f"variance: {objeto.variance_pearson(objeto.yi)}")



