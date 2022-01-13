import requests
import bs4

#res = requests.get("http://nostarch.com")

try:
    # abrindo o arquivo exemplo.html, passando para utf-8
    arquivoDeExemplo = open('exemplo.html', encoding='utf-8')
    # res.raise_for_status()
    # Mastigando para lxml , para o entendimento da maquina
    objectSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")

    # selecionando as tags author
    listAutor = objectSoup.select('#author')

    #   listAutor = objectSoup.select('P')
    #    Pegaria todos os elementos iniciados com <P> , todos os paragrafos

    print('Total de autores' + str(len(listAutor)))
    print('Primeira tag: ' + str(listAutor[0]))
    print('Nome do primeiro autor' + listAutor[0].getText())
except Exception as exc:
    print("Error:%s" % (exc))
