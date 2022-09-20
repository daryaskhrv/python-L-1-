# С использованием страницы https://yandex.ru/images/ сформировать запросы для поиска изображений, 
# контент на которых соответствует классам zebra и bay horse. Для каждого класса должно быть загружено 
# не менее 1000 изображений. Изображения для каждого класса должны находиться в подпапке папки dataset 
# с соответсвующим названием.
#Не допускается:
#Создание папок вручную. В коде должен быть отражен процесс создания папок и перемещения/загрузки в них
#файлов. Дублирование изображений для класса.
#Примечания
#Каждое изображение должно иметь расширение .jpg
#Именовать файлы необходимо порядковым номером (от 0 до 999).
#Для дальнейшего удобства необходимо дополнять имя файла ведующими нулями (например, 0000, 0001, ..., 0999). 
#Для этого необходимо использовать один из методов класса str.
#После загрузки всех изображений, необходимо их просмотреть на соответствие классу. 
#В случае замеченных несоответствий необходимо будет дополнить набор данных до минимального размера. 
#Для избежания подобных ситуаций рекомендуется загружать изображения с запасом.
import os, sys, requests, cv2
from urllib import request
from re import search
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

#https://yandex.ru/images/search?text=zebra
search = {'text' : 'zebra'}
URL = "https://yandex.ru/images/" 
html_page = requests.get(URL + "search", params=search)
# html_page.text - хранит html код веб-страницы
html = BeautifulSoup(html_page.content, "html.parser")
urls = []

def is_valid(url):
     #является ли url допустимым URL
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    for img in html.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # если img не содержит атрибута src, просто пропустите
            continue
        #img_url = urljoin(url, img_url) 
        #сделать URL абсолютным, присоединив домен к только что извлеченному URL
        if is_valid(img_url):
                urls.append(img_url)
    return urls

i = 1
def download(url, pathname):
    global i
    if not os.path.isdir(pathname):
        os.mkdir(pathname)
    request_img = requests.get(url)
    save = open(pathname + "/"+ str(i) + ".jpg", "wb") # открытие потока с типом wb
    i += 1
    save.write(request_img.content) # запись в файл
    save.close() # закрытие файлового потока
    
def main(url, path):
    # получить все изображения
    imgs = get_all_images(url)
    for img in imgs:
        # для каждого изображения, загрузите его
        download(img, path)

main("https://yandex.ru/images/search?text=zebra", "images")