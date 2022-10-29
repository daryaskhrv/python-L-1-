from annotation import Annotation
import os
import shutil


def copy_and_annotation(path_main: str, path: str, ann: Annotation) -> None:
    """Copying dataset to another directory (dataset/class_0000.jpg) and creating an annotation"""
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
            os.rename(os.path.join(path,fname),os.path.join(path, f"{subfolder}_{fname}"))
            ann.add_line(path, f"{subfolder}_{fname}", subfolder)


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    path = 'C:/Users/user/Desktop/dataset1'
    A = Annotation("task2_csv.csv")
    copy_and_annotation(path_main,path,A)