from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd



driver = webdriver.Chrome('C:/chromedriver.exe')
lista_autos = []
for i in range(23):
    url = f'https://autos.mercadolibre.com.ar/0-km/_Desde_{((i*48)+1)}_PciaId_cordoba_NoIndex_True'
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_autos = soup.find_all('li', class_ = 'ui-search-layout__item')
    for auto in all_autos:
        precio = auto.find('span', class_ = 'price-tag-fraction').text.replace('.', '')
        año_km = auto.find('li', class_= 'ui-search-card-attributes__attribute')
        try:
            año = año_km[0].text
        except:
            año = 'Nan'
        try:
            km = año_km[1].text
        except:
            km = 'Nan'
    modelo = auto.find('h2', class_ = 'ui-search-item__title ui-search-item__group__element').text
    locacion = auto.find('span', class_ = 'ui-search-item__group__element ui-search-item__location').text
    link = auto.find('a')['href']
    auto_data = [precio, año, km, modelo, locacion, link]
    lista_autos.append(auto_data)

try:
    df = pd.DataFrame(lista_autos, columns=['precio', 'año', 'km', 'modelo', 'ubicacion', 'link'])
    df.to_excel('autos.xlsx')
    print('Exportación completa')
except:
    print('Error al exportar')
    
    