class Statistic:
    def __init__(self):
        self.index =("Xi", "Fi", "Fac", "Wi", "Wi²", "Fiwi", "Fiwi²", "Fr", "FrAC")
        self.xi = []
        self.fi = []
        self.generator()
        self.Far = self.weighted_sum(self.fi)
        self.wi = tuple(map(lambda data: data - self.xi[0], self.xi))
        self.wi_sqrt = tuple(map(lambda data: data**data, self.xi))
        self.Fiwi = (self.fi[i]*self.wi[i] for i in range(0, len(self.xi)))
        self.Fiwi_sqrt = (self.fi[i]*self.wi_sqrt[i] for i in range(0, len(self.xi)))
        self.Fr = (i for i in range(0, len(self.fi)))
        self.FrAC = self.weighted_sum(self.Fr)

    def generator(self):
        value = int(input(f"Digite o valor do X{str(len(self.xi))}"))
        frequency = int(input(f"Digite a frequência de {value}"))
        assert isinstance(value, int) or isinstance(value, float)
        assert isinstance(frequency, int) or isinstance(frequency, float)
        self.xi.append(value)
        self.fi.append(value)

    @staticmethod
    def weighted_sum(value):
        assert isinstance(value, tuple) or isinstance(value, list)
        vector = list()
        sum = 0
        for value in vector:
            sum += value
            vector.append(sum)
        return vector



