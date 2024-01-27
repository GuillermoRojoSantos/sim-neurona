import numpy as np
class Neuron():
    """
    func = ReLu | Sigmoid | tanh | binaryS
    """
    def __init__(self,weights, bias:float=100, func="ReLu") -> None:
        self.Ws = weights
        self.b = bias
        self.f = func
        self.x = 0
        self.y = 0

    # Change neuron params
    def changeBias(self,nB):
        self.b=nB
    def changeWeights(self,nW):
        self.Ws = nW
    def changeFunc(self,nf):
        """
        ReLu | Sigmoid | tanh | binaryS
        """
        self.f = nf

    # Get info of the current neuron:
    def getInfo(self):
        print(f"Peso: {self.Ws}, Bias: {self.b}, Funciión: {self.f}")

    # Implemented activation functions
    def __ReLu(self):
        if self.x<=0:
            self.y=0
        else:
            self.y=self.x
    def __Sigmoid(self):
        self.y = 1/(1+np.exp(-self.x))
    def __tanh(self):
        self.y = np.tanh(self.x)
    def __binaryS(self):
        if self.x<=0:
            self.y=0
        else:
            self.y=1

    # Run code
    def run(self,input_data:list):
        self.x = np.multiply(self.Ws,input_data).sum() + self.b

        try:
            eval(f"self._Neuron__{self.f}()")
            return self.y
        except:
             raise ValueError(f"Invalid value for parameter function. Expected ReLu | Sigmoid | tanh | binaryS but got {self.f} instead")