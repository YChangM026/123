import pandas as pd
calo = {"첫째":100,"둘째":200,"셋째":300}

#myVar = pd.Series(calo)
myVar = pd.Series(calo, index=["첫째","둘째"])  #* 두 값을 지정함
print(myVar)
print(myVar[0])    #myVar[2] error
print(myVar['둘째'])