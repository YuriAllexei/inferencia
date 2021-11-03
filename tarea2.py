import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
mu,sigma=0,1
lam=2
gamma=4
normal=np.random.normal(loc=mu,scale=sigma,size=45000)   
exp=np.random.exponential(scale=lam,size=45000)
ga = np.random.gamma(shape=1, scale=gamma, size=45000)    
uniforme=np.random.uniform(0,1,45000)

def cor(x):
    x=str(x)
    return int(x[0])
def cortador(x):
    x=str(x)         
    for l in x:
        if l.isdigit() and l!="0":
            return l
def trans(x):
    return 10**x
vfunc=np.vectorize(cortador)
vfunc2=np.vectorize(cor)
vfunc3=np.vectorize(trans)

normalDig=sorted(vfunc(normal))
normalExp=sorted(vfunc(exp))
normalGamma=sorted(vfunc(ga))
uniformeTrans=vfunc3(uniforme)

print(uniformeTrans[:100])

nombres=["Normal","Exponencial","Gamma"]


for i,t in enumerate([normalExp,normalDig,normalGamma]):
    sns.displot(data=t)
    plt.show()

sns.displot(uniformeTrans)
plt.show()

#Podemos ver que en las 4 distribuciones todas se comportan como si fuear una ji-cuadrada con tendencia al 1 lo cual en este caso 
#Verifica que la ley de benson si se cumple

#inciso