# coding : utf-8


import csv 
import requests
from bs4 import BeautifulSoup

fichier = "ListeMammiferes.csv"
fichier = "ListeMammiferes_JHR.csv" ### Je renomme ton fichier pour faire mes tests

url = "https://www.bestioles.ca/liste-mammiferes.html"

# dans l'idée, sortir tous les noms des mammifères

entetes = { 
	"User-Agent":"Ophelie Farissier  -  étudiante à l'UQAM ",
	"From":"phelie07@hotmail.fr"
	}

# pour faire du journalisme non caché 

contenu = requests.get(url,headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser") 

# pour analyser la liste de mammifères qui s'offre à nous

# print(page.find_all("td", valign_="top").find_next("tr"))

# après vérification dans l'URl, ce qui revient c'est "valign = "top" soit l'alignement vertical situé dans tr. j'ai essayé la methode donc du find_next

n = 0

# bestioles = page.find("a", ["href"]).find_next("tr").find_all("td") ### Tu y es presque
### En fait, les infos sur chaque animal sont contenues dans un «tr», alors c'est avec «tr» que tu fais «find_all», car tu veux tous les «tr» (ou toutes les bestioles).
### En examinant attentivement le code HTML, tu pouvais voir que ces «tr» étaient contenus dans une «div» de classe «texte». Donc:
bestioles = page.find("div", class_="texte").find_all("tr")

for bestiole in bestioles:
	n+=1

### Il fallait d'abord contourner une petite difficulté. Certaines lignes du tableau contiennent des pubs.
### Ces pubs ne contiennent pas de balise «a». Donc, si on trouve une balise «a» dans «bestiole», on ramasse l'info, sinon, on ne fait rien et on passe notre chemin :)
	if bestiole.find("a"):

		# print(n, bestioles) ### Ici, imprime plutôt la variable «bestiole» (au singulier)
		print(n, bestiole)

		### Pour trouver le nom, tu l'as! :)
		noms = bestiole.find("a").text.strip() ### Ici, j'ai ajouté «.strip()» pour retrancher des espaces superflus dans certains cas

		### Pour trouver la phrase, petite difficulté
		# phrase = bestiole.find("td").text
		### Chaque «tr» contient 2 «td» de classe identique.
		### Voici une façon de les recueillir.
		### On commence par les chercher tous les deux.
		deuxTD = bestiole.find_all("td")
		### La variable «deuxTD» est une liste. Ce qui t'intéresse se trouve dans le dernier élément de cette liste.
		phrase = deuxTD[1].text.strip()

		### On peut aussi retrancher les «returns» et autres caractères indésirables dans la variable «phrase»
		phrase = phrase.replace("\n","").replace("\r","").replace("  ", " ") ### Il en reste encore, mais c'est déjà ça

		### Pour trouver l'URL, c'est parfait!
		href = bestiole.find("a")["href"]

		infos = [noms, phrase, href]
		print(infos)

# j'ai fait un mélange des deux solutions par rapport aux éléments que j'avais, mais le prompt me signale que l'objet "find_next" n'a pas d'attribu

### Il fallait indenter l'écriture de ton fichier CSV dans ta boucle -> le fichier «ListeMammiferes.csv» te montre ce que ça donne: seulement le dernier mammifère est enregistré
# mammifères = open(fichier, "a") ### Les noms de variables ne peuvent pas prendre d'accents...
# survivants = csv.writer(mammifères) ### No accents por favor :)
		mammiferes = open(fichier, "a")
		survivants = csv.writer(mammiferes)
		survivants.writerow(infos)

# je vais trvailler dessus afin de comprendre mon erreur, mais je suis déja tellement en retard que je vais vous rendre ceci. 
