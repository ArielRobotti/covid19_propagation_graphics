
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlretrieve as retrieve

url="https://covid.ourworldindata.org/data/ecdc/full_data.csv"
retrieve(url,"full_data.csv")
dataset=pd.DataFrame(pd.read_csv('full_data.csv'))

pais="Argentina"

dataPais=dataset.loc[dataset['location']==pais]

casos=list(dataPais.total_cases)
inicio=None
for i in range(len(casos)):
	if casos[i]!=0:
		inicio=i
		break

casos=casos[inicio:]
nuevosCasos=list(dataPais.new_cases)[inicio:]
muertes=list(dataPais.total_deaths)[inicio:]
nuevasMuertes=list(dataPais.new_deaths)[inicio:]
fecha=[]

for i in list(dataPais.date):
	fecha.append(str(i[8:10])+"/"+str(i[5:7]))
fecha=fecha[inicio:]

plt.subplot(2,2,1)

plt.plot(fecha,casos,'o-',color="Black",label="Primer caso registrado el {}".format(fecha[0]))
plt.fill_between(fecha,casos,label="Casos confirmados: {}".format(casos[-1]),color='#ecab43')
plt.grid(True)

plt.title("Graficas covid-19 {}".format(pais))

plt.plot(fecha,nuevosCasos,'o-',color="Black")

plt.fill_between(fecha,nuevosCasos,color='#e9460c',label="Nuevos casos: {}".format(nuevosCasos[-1]))
plt.grid(True)
plt.legend()

plt.subplot(2,2,2)

plt.plot(fecha,muertes,'o-',color="Black")
plt.fill_between(fecha,muertes,label="Muertes: {}".format(muertes[-1]),color='#ecab43')
plt.grid(True)
plt.plot(fecha,nuevasMuertes,'o-',color="Black")
plt.fill_between(fecha,nuevasMuertes,color='#e9460c',label="Nuevas muertes: {}".format(nuevasMuertes[-1]))
plt.xlabel("fecha")
plt.ylabel("Casos")
plt.legend()

plt.subplot(2,2,3)
indice=[]
for i in range(len(casos)):
	try:
		indice.append(muertes[i]*100/casos[i])
	except ZeroDivisionError:
		indice.append(0)

plt.plot(fecha,indice, 'o-',label="Ultimo indice de mortalidad: {}".format(indice[-1]))
plt.legend()

plt.show()
