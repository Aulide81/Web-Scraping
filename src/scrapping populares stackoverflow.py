#Este código esta diseñado para ser ejecutado en un entorno interactivo de Python (IPython).

#Librerias necesarias
import requests
from bs4 import BeautifulSoup
import re
import csv

#Cambiamos el agente
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:74.0) Gecko/20100101 Firefox/74.0"}

##Un poco de navegación
#1. accedemos al home de la web.
web="https://stackexchange.com"
page=requests.get(web,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#2. Hacemos click en Top Users.
link_top_users=soup.find_all('a',string="Top Users")[0].get("href")
page = requests.get(web+link_top_users,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#3. Hacemos click en stack overflow.
link_league_stack=soup.find_all('a',class_="league-site-name",string="Stack Overflow")[0].get("href")
page = requests.get(web+link_league_stack,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#4. Hacemos click en el ranking anual.
link_top_user_stack=soup.find_all('a',string="Year")[0].get("href")
page = requests.get(web+link_top_user_stack,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#5. Hacemos click para obtener los 50 primeros usuarios.
top_50_users=soup.find_all('a',title="show 50 items per page")[0].get("href")
page = requests.get(web+top_50_users,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#6. extraemos los 50 primeros usuarios.
info_50=soup.find_all('div',class_="userInfo")

ranking=soup.find_all('span',class_="number")
pos=ranking[0::4]
pos=[int(i.text.replace("#","")) for i in pos]

change=ranking[1::4]
change=[int(i.text) for i in change]

reputation_total=ranking[2::4]
reputation_total=[int(i.text.replace(",","")) for i in reputation_total]

reputation_year=ranking[3::4]
reputation_year=[int(i.text.replace(",","")) for i in reputation_year]

ranking_values=[]
for i,j,k,l in zip(pos,change,reputation_total,reputation_year):
    ranking_values.append([i,j,k,l])

#Dentro de cada usuario, extraemos informacion sobre sus intervenciones.
#Obtenemos primero el link de su perfil.
data_top_users=[]
for i in range(0,len(info_50)):
    info=info_50[i]
    user_name=info.find('a').text
    user_link=info.find('a')['href']
    data=[user_name,user_link]
    
    insignias=info.find_all('span',class_="badgecount")
    insignias=[int(i.text) for i in insignias]
    data.extend(insignias)
    data.extend(ranking_values[i])
    data_top_users.append(data)
    
#En posesión de los links de los perfiles, accedemos a cada uno de ellos para
#"raspar" la información que creemos más relevante.
for i in range(0,len(data_top_users)):
    url=data_top_users[i][1]
    page=requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    metrics=soup.find_all("div", class_="grid--cell fs-body3 fc-dark fw-bold")
    metrics=[i.text for i in metrics]
    
    metrics=[re.sub('[(),~]', '', i) for i in metrics]
    metrics[0:2]=[int(i) for i in metrics[0:2]]
    
    if "m" in metrics[2]:
        metrics[2]=float(metrics[2].replace("m",""))*1000000
    elif "k" in metrics[2]:
        metrics[2]=float(metrics[2].replace("k",""))*1000
        
    top=soup.find_all("div", id="top-tags")
    total_tags=top[0].find_all("h3")[0].text
    
    for j in ["Top tags (",")",","]:
        total_tags=total_tags.replace(j,"")
        
    total_tags=int(total_tags)
    
    top_tag_info=top[0].find_all("a", class_="post-tag")
    top_tag=top_tag_info[0].text
    
    
    top_tag_metrics=top[0].find_all("div",class_="grid jc-end ml-auto")
    top_tag_metrics=top_tag_metrics[0].find_all("span", class_="fc-medium fs-title")
    top_tag_metrics=[int(i.text.replace(",","")) for i in top_tag_metrics]
    data=[]
    data.extend(metrics)
    data.extend([total_tags,top_tag])
    data.extend(top_tag_metrics)
    data_top_users[i].extend(data)
    
with open('top_50_stackoverflow.csv', mode='w',newline="",encoding="utf-8") as file:
    file_writer = csv.writer(file,delimiter=',')    
    
    file_writer.writerow(["user","href","gold_badges","silver_badges",
                          "bronze_badges","current_position",
                         "change_position","total_reputation",
                         "year_reputation","answers","questions",
                         "people_reached","total_tags","top_tag",
                         "score_top_tag","posts_top_tag",
                         "pct_post_top_tag"])
    
    for i in data_top_users:
        file_writer.writerow(i)
