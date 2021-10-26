import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('seaborn-deep')


def prom(vec):
    return sum(vec)/len(vec)

def momento(vec,mom):
    return sum((vec-prom(vec))**mom)/len(vec)

def curtosis(vec):
    num=momento(vec,4)
    den=momento(vec,2)**2
    return (num/den)-3

def tipo(num,disc):
    
        if num>disc:
            return "leptocúrtica"
        elif num==disc:
            return "mesocúrtica"

        else:
            return "platicúrtica"

def main():
    parametros=((0,1),(0,5),(0,0.4))
    dists=[]
    for l in parametros:
        dists.append(np.random.normal(l[0],l[1],1000))

    curts=list(map(curtosis,dists))

    


    

    
 

    for i in range(len(curts)):
        print("La curtosis es de {0} por lo tanto de tipo {4} para la muestra de {1} elementos de la distribución con parámetros mu={2} y sigma={3}".format(curts[i],len(dists[i]),parametros[i][0],parametros[i][1],tipo(curts[i],0)))


#El tipo de curtosis a la cuales pertenecen es bastante errática al menos con estos parámetros pero al graficarlos si se ve bastante claro las diferencias uno a uno
#Siento que para poder tener una decisión más estricta deberíamos de simular y al final ver a cual pertenecen en promedio dados los mismos parámetros



if __name__=="__main__":
    main()