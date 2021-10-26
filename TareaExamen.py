import numpy as np
import pandas as pd
from collections import OrderedDict



#Inciso 2

def promedio(x):
    return sum(x)/len(x)

def desvEst(x):
    return varianza(x)**0.5
def varianza(x):
    return (sum((x-promedio(x))**2))/(len(x)-1)

def rangoMuestral(x):
    return max(x)-min(x)


def momento(vec,mom):
    return sum((vec-promedio(vec))**mom)/(len(vec)-1)


def curtosis(vec):
    num=momento(vec,4)
    den=momento(vec,2)**2
    return (num/den)-3

def skew(x):
    num=momento(x,3)
    den=momento(x,2)**(1.5)
    return num/den


def percentiles(x):
    return np.percentile(x,[25,75])

def mediana(x):
    x=sorted(x)
    if len(x)%2!=0:
        return x[(len(x)+1)//2]
    else:
        return (x[len(x)//2]+x[(len(x)//2)+1])/2


def notNA(x):
    return x.isnull().sum()


def vectorFunc(L,x,r):
    for f in L:
        r.append(f(x))
    return r


def limpieza1(col1,relleno=None):
    if pd.isnull(col1):
        return relleno
    else:
        return col1


def limpieza2(col1,col2 ): #Col1=Rear col2=Passengers
    if col2==2:
        return 0
    else: return col1

def cuentasUnicas(x):
    cuentas={}
    columnas=x.columns
    for col in columnas:
        sub={}
        actual=x[col]
        for boom in actual:
            if boom not in sub.keys():
                sub.setdefault(str(boom),1)
            else:
                sub[str(boom)]+=1
        cuentas[col]=sub

    return cuentas   

    # for cat in x:
    #     if cat not in cuentas.keys():
    #         cuentas.setdefault(str(cat),1)
    #     else:
    #         cuentas[str(cat)]+=1
    # return cuentas

def modas(x,n):

    campeones={}
    for ca in x.keys():
        bam=x[ca]
        target=max(bam.values())
        acep={}
        for punto,cu in bam.items():
            if cu==target and len(acep)<n:
                acep[punto]=cu
        campeones[ca]=acep
    return campeones

def tablaResumen(data):
    dataNum=data.select_dtypes(include=["float64","int64"])
    resumen={}
    columnas=dataNum.columns[1:]
    for col in columnas:
        L=[min,percentiles,mediana,promedio,max,rangoMuestral,varianza,desvEst,skew,curtosis,notNA]
        r=vectorFunc(L,dataNum[col],[])
        resumen[col]=r
    return pd.DataFrame.from_cuentast(resumen,orient='index',columns=["Mín","Q1Q3","Mediana","Promedio","Máx","RangoMuestral","Varianza","STD","Sesgo","Curtosis","NaN´s"]).T

def frecAbs(x):
    nuevo={}
    for i in x.keys():
        nuevo[i]=[x[i],sum(x[i].values())]

    return nuevo


def frecAcum(x):
    acumulada={}
    for col in x.keys():
        actual=x[col][0]
        temp=0
        neo={}
        for cosa,num in actual.items():
            temp+=num
            neo[cosa]={num:temp}
        acumulada[col]=neo
        if temp==absoluta[col][1]:
            temp=0   
    return acumulada

def frecRelativa(x):
    frecuenciaRel={}
    for cat in x.keys():
        actual=x[cat]
        nuevo={}
        cuentasinterno=actual[0]
        total=actual[1]
        for cosa,num in cuentasinterno.items():
            nuevo[str(cosa)]=(num/total)*100
        frecuenciaRel[str(cat)]=nuevo


    return frecuenciaRel
def impFrecRel(frec):
    print("Frecuencia Relativa:")
    for cat,f in frec.items():
        print("Observación {0}:".format(cat))
        temp=0
        for punto,rel in f.items():
            string=punto.ljust(30," ")
            ar=round(rel,5)
            print("{0}   {1}".format(string,ar))
            temp+=ar
        print("Porcentaje total: {}".format(temp))



def impFrecAbs(frec):
    print("Frecuencia absoluta:")
    for cat,p in frec.items():
        print("Observación:{}\n".format(cat))
        cs=p[0]
        tot=p[1]
        print("Individuo             Cuenta")
        for pn,cu in cs.items():
            string=pn.ljust(18)
            cu=str(cu)
            print("{0}   {1}".format(string,cu))
        print("Total para {0}: {1}\n".format(cat,tot))


def imprFrecAc(frec):
    print("Frecuencia acumulada:")
    for i in frec.keys():
        actual=frec[i]
        print("Observación actual: {0}".format(i))
        print("Individuo           Cuenta  Acumulado")
        suma=0
        for p,v in actual.items():
            string=p.ljust(20," ")
            print(v)
            n=""
            ac=""
            for a,b in v.items():
                n=a
                ac=b
            print("{0}  {1}   {2}".format(string,n,ac))
            suma+=n
        print("Total acumulado de {0}: {1}".format(i,suma))

#Convirtiendo la columna de Cylinders a numérica pues la identifica como object
data=pd.read_csv("Cars93.csv")
data["Cylinders"]=data["Cylinders"].replace("rotary","4")
data["Cylinders"]=data["Cylinders"].apply(int)



# tablaSucia=tablaResumen(data)
# print("Tabla de resumen con data sin limpiar:\n",tablaSucia)


# #Limpiamos la data
# data['Rear.seat.room'] = data.apply(lambda x : limpieza2(x["Rear.seat.room"],x["Passengers"]),axis=1)
# data['Luggage.room'] = data.apply(lambda x: limpieza1(x['Luggage.room'], max(data["Luggage.room"])), axis=1)
# tablaLimpia=tablaResumen(data)
# print("Tabla de resumen con data limpia",tablaLimpia)



#inciso 3

dataCat=data.select_dtypes(include=["object"])
print(cuentasUnicas(dataCat))
print("Modas:\n",modas(cuentasUnicas(dataCat),3))

absoluta=frecAbs(cuentasUnicas(dataCat))
#Frecuencia absoluta:




#Frecuencia acumulada:
acumulada=frecAcum(absoluta)
print("Frecuencia acumulada\n\n\n\n\n",acumulada)

#Frecuencia relativa:
frecRel=frecRelativa(absoluta)

impFrecRel(frecRel)
impFrecAbs(absoluta)
imprFrecAc(acumulada)