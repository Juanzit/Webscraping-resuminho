import requests
import bs4
import webbrowser
termoBuscado = input("O que deseja?")
print("Buscando termo" + termoBuscado)

# Requisição ao  buscador do google
res = requests.get('https://www.google.com/search?q=' + termoBuscado)

res.raise_for_status()

# bs4 analisa o html da pagina retornada
soup = bs4.BeautifulSoup(res.text, features="lxml")

# receber uma lista com links das primeiras páginas retornadas
linksList = soup.select('.r a')
# tudo dentro da "div class r" , buscando o "a" que contem o link em si

#seleciono o menor número, que pode ser 5 ou o número de links retornados
numPagesOpen = min(5, len(linksList))

#print(linksList[0])
#print(linksList[0].get('href'))

#para cada link retornado da busca do google 
for i in range(numPagesOpen):
    #[7:] ignora os 7 primeiros caracteres
    print("Opening " + linksList[i].get('href') [7:]+ "\n")

    #abrir 5 abas contendos os 5 links
    webbrowser.open('http://google.com' + linksList[i].get('href'))

print("Done.")
