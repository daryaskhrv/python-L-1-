#1.Написать скрипт для формирования текстового файла-аннотации собранного датасета. Файл-аннотация 
#   должен представлять собой csv-файл, в котором в первой колонке будет указан абсолютный путь к файлу, 
#   во второй колонке относительный путь относительно вашего Python-проекта, третья колонка будет 
#   содержать текстовое название класса (метку класса), к которому относится данный экземпляр.
#2.Написать скрипт для копирования датасета в другую директорию таким образом, чтобы имена файлов 
#   содержали имя класса и его порядковый номер. То есть из dataset/class/0000.jpg должно получиться 
#   dataset/class_0000.jpg.
#3.Написать скрипт, создающий копию датасета таким образом, чтобы каждый файл из сходного датасета 
#   получил случайный номер от 0 до 10000, и датасет представлял собой следующую структуру 
#   dataset/номер.jpg. Для того чтобы осталась возможность определить принадлежность экземпляра к классу
#   создать файл-аннотацию (как в пункте 1).
#4.Написать скрипт, содержащий функцию, получающую на входе метку класса и возвращающую следующий 
#   экземпляр (путь к нему) этого класса. Экземпляры идут в любом порядке, но не повторяются. Когда 
#   экземпляры заканчиваются, функция возвращает None. Данная функция должна быть в трёх версиях для 
#   пунктов 1–3.
#5.Написать на основе предыщего пункта классы итераторы (пример ниже).

import csv, os, shutil, random

#print('Текущая директория - ',os.getcwd ())


#for dirs, folder, files in os.walk(path):
    #print('Выбранный каталог - ', dirs)
    #print('Вложенные папки - ', folder)
    #print('Файлы в папке - ', files)
    #for file in files:
       # print('Полный путь к файлу - ', os.path.join(dirs,file))
       # print('Относительный путь к файлу - ',os.path.relpath(os.path.join(dirs,file)))
   # print('\n')
    
def creatAnnotation(path):
    """Creating an annotation for dataset"""
    file_name = "task1_csv.csv"
    with open(file_name, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow(["Абсолютный путь", "Относительный путь", "Метка"])
        folders = []
        i=0
        for dirs, folder, files in os.walk(path):
            if i==0:
                folders = folder
            else:
                for file in files:
                    writer.writerow([os.path.join(dirs,file), os.path.relpath(os.path.join(dirs,file)), folders[i-1]])
            i+=1
            print('\n')
        

def task2(path_main, path):
    """Copying dataset to another directory (dataset/class_0000.jpg) and creating an annotation"""
    file_name = "task2_csv.csv"
    with open(file_name, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow(["Абсолютный путь", "Относительный путь", "Метка"])
        subfolders = os.listdir(path_main)
        for subfolder in subfolders:
            files=os.listdir(os.path.join(path_main,subfolder))
            for fname in files:
                shutil.copy(os.path.join(path_main,subfolder,fname),path)
                os.rename(os.path.join(path,fname),os.path.join(path, f"{subfolder}_{fname}"))
                writer.writerow([os.path.join(path, f"{subfolder}_{fname}"),os.path.relpath(os.path.join(path, f"{subfolder}_{fname}")),subfolder])


def task3(path_main, path):
    """Copying dataset to another directory (dataset/номер.jpg) and creating an annotation"""
    file_name = "task3_csv.csv"
    with open(file_name, "w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow(["Абсолютный путь", "Относительный путь", "Метка"])
            subfolders = os.listdir(path_main)
            for subfolder in subfolders:
                files=os.listdir(os.path.join(path_main,subfolder))
                for fname in files:
                    shutil.copy(os.path.join(path_main,subfolder,fname),path)
                    fname2 = f"{random.randint(0, 10000)}.jpg"
                    os.rename(os.path.join(path,fname),os.path.join(path, fname2))
                    writer.writerow([os.path.join(path, fname2),os.path.relpath(os.path.join(path, fname2)), subfolder])



if __name__ == "__main__":
    path_main = os.path.join('C:/','Users','user','Desktop','dataset_copy')
    path1 = 'C:/Users/user/Desktop/dataset1'
    path2 = 'C:/Users/user/Desktop/dataset2'
    creatAnnotation(path_main)
    task2(path_main, path1)
    task3(path_main, path2)
