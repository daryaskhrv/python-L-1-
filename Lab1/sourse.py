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
import os, requests
from urllib import request
from re import search
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    '''Проверяет, является ли url допустимым URL'''
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url, key):
    '''Возвращает определенное количество URL‑адресов изображений по одному `url`'''
    urls = []
    page = 1
    while True:
        URL = url + "search?p=" + str(page) + "&text=" + key
        html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
        html = BeautifulSoup(html_page.content, "html.parser")
        for img in html.find_all("img"):
            img_url = img.attrs.get("src")
            if not img_url:
                continue
            img_url = urljoin(URL, img_url) 
            #сделать URL абсолютным, присоединив домен к только что извлеченному URL
            if is_valid(img_url):
                    urls.append(img_url)
        page += 1
        if len(urls) > 1100: 
            break
    return urls

def download(url, pathname, index): 
    '''Загружаем одно изображение по адресу `url` в папку'''
    if not os.path.isdir(pathname):
        os.mkdir(pathname)
    request_img = requests.get(url)
    save = open(pathname + "/"+ str(index).zfill(4) + ".jpg", "wb") 
    save.write(request_img.content) 
    save.close()   

def get_and_download(url, key):
    '''Вызывает основные функции, возвращает кол-во изображений для одного key'''
    imgs = get_all_images(url, key)
    i = 1 
    for img in imgs:
        download(img, key, i)
        i += 1
    return i
    


def main(url):
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    os.chdir("dataset")
    key1 = "zebra"
    key2 = "bay horse"
    amount1 = get_and_download(url, key1)
    print("Successfully uploaded " + str(amount1) + " "+ key1 + " images.")
    amount2 = get_and_download(url, key2)
    print("Successfully uploaded " + str(amount2) + " "+ key2 + " images.")
    

main("https://yandex.ru/images/")
