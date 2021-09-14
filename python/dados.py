from bs4 import BeautifulSoup
import requests
import pandas as pd

sop = BeautifulSoup(requests.get('https://www.scrapethissite.com/pages/simple/').text, 'html.parser')

pais = []
capital = []
populacao = []
area = []

sop_pais = sop.find_all('h3', class_= 'country-name') 

sop_capital = sop.find_all('span', class_='country-capital')

sop_populacao = sop.find_all('span', class_='country-population')

sop_area = sop.find_all('span', class_='country-area')

for i in sop_pais:       pais.append(i.text.strip())

for i in sop_capital:   capital.append(i.text.strip())

for i in sop_populacao: populacao.append(i.text.strip())

for i in sop_area:      area.append(i.text.strip())

#---------------------------------------------
with open('src/paises.xlsx','w', encoding="utf-8") as f: #Sempre utilizar encoding para o reconhecimento. 

    f.write(f'PAÍSES\tCAPITAL\tPOPULAÇÃO\tAREA\n') #TITULO --- Primeira linha das colunas

    for pa,ca,po,ar in zip(pais,capital,populacao,area): #Dados a receber

        ca.replace('ş','s').replace('ă','') #String de enconding desconhecidos... Fazendo que evite erros

        f.write(f'{pa}\t{ca}\t{po}\t{ar}\n') #Imprimindo os    