from bs4 import BeautifulSoup
import requests, sqlite3


#CRIANDO BANCO DE DADOS
conn = sqlite3.connect('db/paises.db') #Criando conexão e o banco de dados
c = conn.cursor() #inserindo método cursor


#OBTENDO A RASPAGEM
sop = BeautifulSoup(requests.get('https://www.scrapethissite.com/pages/simple/').text, 'html.parser')

#LISTAS A RECEBER DADOS
pais = []
capital = []
populacao = []
area = []

#CRIANDO MÉTODO PARA EXTRAÇÃO DE CADA DADOS REFERENTE AS LISTAS CRIADAS
sop_pais = sop.find_all('h3', class_= 'country-name') #TAG + CLASS

sop_capital = sop.find_all('span', class_='country-capital')

sop_populacao = sop.find_all('span', class_='country-population')

sop_area = sop.find_all('span', class_='country-area')


#INSERINDO VALORES A LISTAS
for i in sop_pais:
    pais.append(i.text.strip()) #ponteiro + acrescentar valor a lista (ponteiro+ texto+ conjuntos de caracteres)

for i in sop_capital:
    capital.append(i.text.strip())

for i in sop_populacao:
    populacao.append(i.text.strip())

for i in sop_area:
    area.append(i.text.strip())

#AGRUPANDO EM FOR ZIP ÍNDICES SEMELHANTES     
#INSERINDO NO BANCO DE DADOS
for pa, ca, po, ar in zip(pais, capital, populacao, area):
    c.execute(f"INSERT INTO WEBSCRAPING(PAIS,CAPITAL,POPULACAO,AREA) VALUES(\"{pa}\",\"{ca}\",{po},{ar});")

c.execute("COMMIT;")
conn.close()                                                                                                                    
                                                                                                              