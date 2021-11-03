#Tareita 2 ley de Benford

##Dada  x1,...,xn una muestra aleatoria de tamaño n proveniente de alguna distribución F, exteraer el primer digito
##No cero despues del punto decimal y verificar graficamente si la nueva muestra tiene un comportamiento similar a lo que indica
##La ley de Benford. Pej; si el numero simulado es  x=o.oo234 el digito que deseamos recuperar es d=2
###Analizar el comportamiento de las sig dist.
###Finalmente, tomar Y=10^X Tq X~U(1,0) y extraer el digito antes del pto decimal y analisar el comportamiento
###de la muestra obtenida.

import numpy as np
from numpy.random.mtrand import uniform
import seaborn as sns
import matplotlib.pyplot as plt 

def trans1(x):
    x=str(x)         
    for l in x:
        if l in ["1","2","3","4","5","6","7","8","9"] and l!="0":
            return int(l)




#Consideremos n>30,000
N=np.random.normal(loc=0,scale=1,size=50000)   
E=np.random.exponential(scale=2,size=50000)
G= np.random.gamma(shape=1, scale=4, size=50000)    
U=np.random.uniform(0,1,50000)

f=np.vectorize(trans1)

y=np.vectorize(lambda x:10**x)

normal=np.array(f(N))
exponencial=np.array(f(E))
gamma=np.array(f(G))
uniforme=np.array(y(U))


d=[normal,exponencial,gamma,uniforme]

for i in range(4):
    sns.displot(data=d[i])
    plt.show()


##Conclusiones: Podemos notar que a lo que la ley de Benford se refiere, sí es el número 1 con mas frecuencia
##que el resto de los numeros. Ya que por medio de los gráficos se comprueba que si es el numero 1 el que aparece más.