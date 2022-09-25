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

def is_valid(url): #является ли url допустимым URL
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url, key):
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
        if len(urls) > 50: 
            break
    return urls

def download(url, pathname, index): 
    if not os.path.isdir(pathname):
        os.mkdir(pathname)
    request_img = requests.get(url)
    save = open(pathname + "/"+ str(index).zfill(4) + ".jpg", "wb") 
    save.write(request_img.content) 
    save.close() 

def cmp(image_1: cv2.Mat, image_2: cv2.Mat) -> bool:
    return image_1 == image_2   

def get_and_download(url, key):
    imgs = get_all_images(url, key)
    i = 1 
    for img in imgs:
        download(img, key, i)
        i += 1
    return i
    '''k=1
    while k<i:
        print("ijdij",os.getcwd())
        srttmp = os.getcwd
        str = srttmp + "/"+ "zebra" + "/"+str(k).zfill(4) + ".jpg"
        print(str)
        image_1 = cv2.imread('C:/Users/user/python-L-1-/dataset/zebra/0003.jpg')
        cv2.imshow('window_name', image_1) 
        cv2.waitKey(0)
        k = 1200'''


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
    
    '''image = cv2.imread('C:/Users/user/python-L-1-/dataset/zebra/0003.jpg')  
    print(image.shape) 
    #cv2.imshow('window_name', image) 
    #cv2.waitKey(0)

    image_1 = cv2.imread("dataset/zebra/0010.jpg")
    image_2 = cv2.imread("dataset/zebra/0020.jpg")
    tmp = cmp(image_1, image_2)
    if tmp == False:
        print("Yes")
    else:
        print("No")'''

main("https://yandex.ru/images/")
