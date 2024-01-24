import numpy as np
class Neuron():
    def __init__(self,weights:list, bias:float=100, func="relu") -> None:
        self.Ws = weights
        self.b = bias
        self.f = func
        self.x = 0
        self.y = 0

    def changeBias(self,nB):
        self.b=nB

    def __ReLu(self):
        if self.x<=0:
            self.y=0
        else:
            self.y=self.x
    def __Sigmoid(self):
        self.y = 1/(1+np.exp(-self.x))
    def __tanh(self):
        self.y = np.tanh(self.x)

    def changeWeights(self,nW):
        self.Ws = nW

    def run(self,input_data:list):
        self.x = np.multiply(self.Ws,input_data).sum() + self.b

        try:
            eval(f"self._Neuron__{self.f}()")
            return self.y
        except:
             raise ValueError(f"Invalid value for parameter function. Expected ReLu | Sigmoid | tanh but got {self.f} instead")