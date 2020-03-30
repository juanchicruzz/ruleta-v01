import random
from matplotlib import pyplot as plt # Importamos los módulos necesarios
from matplotlib import numpy as np 
import pandas as pd

tiradas=[10,100,1000,10000,100000]
variancias=[]
desvios=[]

for q in range(0,len(tiradas)):
    wins = []
    n = tiradas[q]
    for i in range(n):
        win_number = random.randint(0,36)
        wins.append(win_number)
    #print ("Los numeros ganadores son ", wins)
    print ( "---------------------------------------" )

    #FRECUENCIA ABSOLUTA
    p = list(range(0,37))
    f = list(range(37))
    #print(p)

    for i in range(0,37):
        co=0
        for j in range(0,len(wins)):
            if p[i] == wins[j]:
                co=co+1
        f[i]=co

    #print(f)
    #print(sum(f))

    #FRECUENCIA RELATIVA

    fre=list(range(37))
    for i in range(0,37):
      fre[i]=f[i]/n

    #print (fre)
    #print (sum(fre))

    desv=np.std(wins)
    varian=np.var(wins)


    variancias.append(varian)
    desvios.append(desv)

    plt.plot(fre)
    plt.show()



plt.plot(tiradas,variancias)
plt.plot()
plt.show()
