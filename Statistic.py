import numpy as np
import pandas as pd
import math



# gerente - > modulos com partes da estatistica
class Statistic:
    """
        0 = variance table
        1 = cumulative frequency table by class
        2 = cumulative frequency table by class
    """
    def __init__(self, key):
        if key == 0:
            self.xi = [7, 5, 6, 6, 6, 4, 8, 6, 9, 3]
            self.xi_sqrt = [i * i for i in self.xi]
            self.yi = [20, 14, 18, 18, 17, 11, 25, 19, 26, 10]
            self.yi_sqrt = [i * i for i in self.yi]
            self.xiyi = [self.xi[i] * self.yi[i] for i in range(0, len(self.xi))]
            self.tables(key)

        if key == 1:
            self.value_inf = [12.5, 13.5, 14.5, 15.5, 16.5, 17.5]
            self.value_sup = [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
            self.value_class = [f"{self.value_inf[i]}|--{self.value_sup[i]} " for i in range(0, len(self.value_inf))]
            self.xi = [(self.value_inf[i] + self.value_sup[i]) / 2 for i in range(0, len(self.value_inf))]
            self.xi_sqrt = [i * i for i in self.xi]
            self.fi = [7, 13, 19, 24, 15, 2]
            self.fixi = [self.xi[i] * self.fi[i] for i in range(0, len(self.xi))]
            self.far = self.weighted_sum(self.fi)[0]
            self.wi = [i - self.xi[0] for i in self.xi]
            self.wi_sqrt = [i * i for i in self.wi]
            self.fiwi = [self.fi[i] * self.wi[i] for i in range(0, len(self.xi))]
            self.fiwi_sqrt = [self.fi[i] * self.wi_sqrt[i] for i in range(0, len(self.xi))]
            self.fr = [i / self.far[1] for i in self.fi]
            self.frac = self.weighted_sum(self.fr)[0]
            self.tables(key)

        if key == 2:
            self.xi = [14]
            self.xi_sqrt = [i * i for i in self.xi]
            self.fi = [7, 13, 19, 24, 15, 2]
            self.fixi = [self.xi[i] * self.fi[i] for i in range(0, len(self.xi))]
            self.far = self.weighted_sum(self.fi)[0]
            self.wi = [i - self.xi[0] for i in self.xi]
            self.wi_sqrt = [i * i for i in self.wi]
            self.fiwi = [self.fi[i] * self.wi[i] for i in range(0, len(self.xi))]
            self.fiwi_sqrt = [self.fi[i] * self.wi_sqrt[i] for i in range(0, len(self.xi))]
            self.fr = [i / self.far[1] for i in self.fi]
            self.frac = self.weighted_sum(self.fr)[0]
            self.tables(key)



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


    def tables(self, key=1):
        if key == 0:
            self.table = {"xi": self.xi,
                          "yi": self.yi,
                          "xi²": self.xi_sqrt,
                          "yi²": self.yi_sqrt,
                          "xiyi": self.xiyi}

            self.summation = {"Index": "Value",
                              "Σ(xi)": self.weighted_sum(self.xi)[1],
                              "Σ(yi)": self.weighted_sum(self.yi)[1],
                              "Σ(xi²)": self.weighted_sum(self.xi_sqrt)[1],
                              "Σ(yi²)": self.weighted_sum(self.yi_sqrt)[1],
                              "Σ(xiyi)": self.weighted_sum(self.xiyi)[1]}

            self.df = pd.DataFrame(self.table)
            self.df_00 = pd.DataFrame(self.summation, index=[0])
            print(self.df)
            print(self.df_00)

        elif key == 1:
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

        elif key == 2:
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


    def generator_csv(self):
        pass


    def variance_x(self):
        n = len(self.xi)
        return (self.weighted_sum(self.xi_sqrt)[1] - (1 / n) * (self.weighted_sum(self.xi)[1] ** 2))/n


    def variance_y(self):
        n = len(self.yi)
        return (self.weighted_sum(self.yi_sqrt)[1] - (1 / n) * (self.weighted_sum(self.yi)[1] ** 2))/n

    #alterações na covariancia de pearson / n assim como as variancias normais
    def r_pearson(self):
        n = len(self.xi)
        sum_xiyi = self.weighted_sum(self.xiyi)[1]
        sum_xi = self.weighted_sum(self.xi)[1]
        sum_yi = self.weighted_sum(self.yi)[1]
        cov_xy = (sum_xiyi - (1/n)*sum_xi*sum_yi)/n
        var_x = self.variance_x()
        var_y = self.variance_y()
        return cov_xy/math.pow(var_x * var_y, 1/2)


    def classification_r_pearson(self):
        value = self.r_pearson()
        if 0 <= value <= 0.19:
            return "Muito Fraca"
        elif 0.20 <= value <= 0.39:
            return "Fraca"
        elif 0.40<= value <= 0.69:
            return "Moderada"
        elif 0.70<= value <= 0.89:
            return "Forte"
        elif 0.90<= value <= 1:
            return "Muito Forte"


    def standard_deviation(self):
        return math.pow(self.variance(), 1/2)


    def covariance(self, vector_x, vector_y):
        pass


if __name__ == '__main__':
    objeto = Statistic(0)
    print(f"variance: {objeto.variance_x()}")
    print(f"covariancia: {objeto.r_pearson()}")
    print(objeto.classification_r_pearson())

