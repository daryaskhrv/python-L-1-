from annotation import Annotation
import os
import shutil
import random 


def random_copy(path_main: str, path: str, ann: Annotation) -> None:
    """Copying dataset to another directory (dataset/номер.jpg) and creating an annotation"""
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
    subfolders = os.listdir(path_main)
    for subfolder in subfolders:
        files=os.listdir(os.path.join(path_main,subfolder))
        for fname in files:
            shutil.copy(os.path.join(path_main,subfolder,fname),path)
            fname2 = f"{random.randint(0, 10000)}.jpg"
            while os.path.isdir(os.path.join(path, fname2)):
                fname2 = f"{random.randint(0, 10000)}.jpg"
            os.rename(os.path.join(path,fname),os.path.join(path, fname2))
            ann.add_line(path,fname2,subfolder)


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    path = 'C:/Users/user/Desktop/dataset2'
    A3 = Annotation("task3_csv.csv")
    random_copy(path_main,path,A3)