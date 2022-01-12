import requests
# Guardando a pagina em que quero extrair uma informação , na variavel res
res = requests.get("https://pypi.org/project/selenium/")

# O try serve pra testar um bloco de codigo verificando se à erro
try:
    res.raise_for_status()
    file = open("Selenium.txt", "wb")
    # Abrindo arquivo.txt para salvar o conteudo
    # wb , w = poder de escrita , b = escrita em binário
    for chunck in res.iter_content(100000):
        file.write(chunck)
        # Adicionando de 100000 em 100000 ate o arquivo conter os componentes do link

except Exception as exc:
    print("Error:%s" % (exc))
# Se nenhuma exceção ocorrer (der Erro), a cláusula except será ignorada e a execução da instrução try será concluída.
