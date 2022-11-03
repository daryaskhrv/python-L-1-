from annotation import Annotation
import os


def creat_annotation(path: str, ann: Annotation) -> None:
    """Creating an annotation for main dataset"""
    folders = []
    i=0
    for dirs, folder, files in os.walk(path):
        if i==0:
            folders = folder
        else:
            for file in files:
                ann.add_line(dirs,file,folders[i-1])
        i+=1 


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    A = Annotation("task1_csv.csv")
    creat_annotation(path_main, A)        