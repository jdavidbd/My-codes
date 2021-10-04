from bs4 import BeautifulSoup
import requests


url = "https://www.supercarros.com/carros/cualquier-tipo/cualquier-provincia/Toyota/?PagingPageSkip=41"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(id="bigsearch-results-inner-lowerbar-pages")
pages = int(str(page_text).split("40")[-1].split("a")[0].split(">")[-1][:2])

for page in range(0, pages+1):
    url = f"https://www.supercarros.com/carros/cualquier-tipo/cualquier-provincia/Toyota/?PagingPageSkip={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    busqueda = doc.find_all(class_="title1")
    modelo = list()

    for i in busqueda:
        modelo.append(i.text)
        print(modelo)
        
