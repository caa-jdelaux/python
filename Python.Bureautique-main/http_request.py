import requests
import html

url = "https://github.com/ZorroLeVrai/Python.Bureautique/blob/main/Exemples/vus_en_cours/liste_fibonacci_bis.py"

contenu = requests.get(url)
print(contenu.text)

#print(dir(requests))
# print(help(contenu.text))