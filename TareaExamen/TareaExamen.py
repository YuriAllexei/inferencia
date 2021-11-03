import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


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

    for cat in x:
        if cat not in cuentas.keys():
            cuentas.setdefault(str(cat),1)
        else:
            cuentas[str(cat)]+=1
    return cuentas

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
    return pd.DataFrame.from_dict(resumen,orient='index',columns=["Mín","Q1Q3","Mediana","Promedio","Máx","RangoMuestral","Varianza","STD","Sesgo","Curtosis","NaN´s"]).T

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

def imprimeModas(x):
    for k,v in x.items():
        print("Modas para {}".format(k))
        for ll,val in v.items():
            print("{0}  {1}".format(ll,val))

for i in range(5,9):
    os.makedirs("TareaExamen/incisos/inciso{0}".format(i))
    
    
#inciso 2
data=pd.read_csv("TareaExamen/Cars93.csv")
data["Cylinders"]=data["Cylinders"].replace("rotary","5")
data["Cylinders"]=data["Cylinders"].apply(int)


tablaSucia=tablaResumen(data)
print("Inciso 2:\nTabla de resumen con data sin limpiar:\n",tablaSucia)
#Limpiamos la data
data['Rear.seat.room'] = data.apply(lambda x : limpieza2(x["Rear.seat.room"],x["Passengers"]),axis=1)
data['Luggage.room'] = data.apply(lambda x: limpieza1(x['Luggage.room'], max(data["Luggage.room"])), axis=1)
tablaLimpia=tablaResumen(data)
print("Tabla de resumen con data limpia",tablaLimpia)


#inciso 3
print("Inciso 3:\n")
dataCat=data.select_dtypes(include=["object"])
print("Modas:")
print(imprimeModas(modas(cuentasUnicas(dataCat),3)))

absoluta=frecAbs(cuentasUnicas(dataCat))
#Frecuencia absoluta:

#Frecuencia acumulada:
acumulada=frecAcum(absoluta)
print("Frecuencia acumulada\n\n",acumulada)

#Frecuencia relativa:
frecRel=frecRelativa(absoluta)

impFrecRel(frecRel)
impFrecAbs(absoluta)
imprFrecAc(acumulada)


#inciso 4

#Tabulamos conjuntamente 2 dataframes distinas, la primera separando a partir de Type AirBags y la segunda por Cylinders,Man.trans.avail y las analizamos a partir de la 
#media, mínimo, max y la desviación estandar del precio.  
conjunta1 = data.groupby(["Type","AirBags"]).agg({'Price': ['mean', 'min', 'max',"std"]})
conjunta2 = data.groupby(["Cylinders","Man.trans.avail"]).agg({'Price': ['mean', 'min', 'max',"std"]})
print("Inciso 4:")
print(conjunta1,"\n\n\n\n")
print(conjunta2)


#inciso 5

cuantitativas=data.select_dtypes(include=(["float64","int64"]))
nombres=[x for x in cuantitativas.columns][1:]
colores=["Accent", "Accent_r", "Blues", "Blues_r", "BrBG", "BrBG_r", "BuGn", "BuGn_r", "BuPu", "BuPu_r", 
 "CMRmap", "CMRmap_r", "Dark2", "Dark2_r", "GnBu", "GnBu_r", "Greens", "Greens_r", "Greys", "Greys_r", "OrRd", 
 "OrRd_r", "Oranges", "Oranges_r", "PRGn", "PRGn_r", "Paired", "Paired_r"]


for c,i in enumerate(nombres):
    fig, ax = plt.subplots()
    sns.set_palette("{}".format(colores[c]))
    sns.boxplot(data=cuantitativas[i]).set(title='Boxplot de {0}'.format(i), xlabel='{}'.format(i))
    plt.savefig("TareaExamen/incisos/inciso5/boxplot{}.png".format(i))
    plt.close()
    
    
    
    
#inciso 6

sns.boxplot(y="Max.Price",x="Cylinders",data=cuantitativas,palette="PRGn")
plt.savefig("TareaExamen/incisos/inciso6/PrecioMaximoCilindros.png")
plt.close()

#Inciso 7
sns.boxplot(y="Horsepower",x="Cylinders",data=cuantitativas,palette="PRGn")
plt.savefig("TareaExamen/incisos/inciso7/CilindrosCaballos")
plt.close()


#inciso 8

corrs=cuantitativas[["Length","Width","Wheelbase","Rear.seat.room","Luggage.room"]]

corrdf=corrs.corr()


print("Inciso 8:\nTabla de correlaciones:")
print(corrdf)
sns.heatmap(corrdf, annot=True)
plt.savefig("TareaExamen/incisos/inciso8/TablaCorrelaciones.png")
plt.close()
