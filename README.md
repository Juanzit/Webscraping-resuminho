# Webscraping 

----------------------------------------------------------------
import requests
res = requests.get("https://pypi.org/project/selenium/")

try:
    res.raise_for_status()
    print("Check")
    file = open("Selenium.txt", "wb")
    for chunck in res.iter_content(100000):
        file.write(chunck)

except Exception as exc:
    print("Error:%s" % (exc))
---------------------------------------------------------------
