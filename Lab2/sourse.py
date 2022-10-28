import csv, os, shutil, random, pandas
from itertools import count


class Annotation:

    def __init__(self,file_name: str) -> None:
        self.number_lines = 0
        self.viewed_files = 1
        self.file_name = file_name

    def add_line(self, path: str, fname: str, label: str) -> None: 
        """Addind a line to an annotation"""
        with open(self.file_name, "a", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            if self.number_lines == 0:
                writer.writerow(["Абсолютный путь", "Относительный путь", "Метка"])
                self.number_lines+=1
            writer.writerow([os.path.join(path, fname),os.path.relpath(os.path.join(path, fname)), label])
            self.number_lines+=1
            fh.close()

    def next(self, label: str) -> str:
        """Returns the next instance of annotation by label without repetition"""
        with open(self.file_name, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter = ",")
            count = 0
            for row in file_reader:
                if count < self.viewed_files:
                    count+=1
                elif self.viewed_files < self.number_lines:
                    self.viewed_files+=1
                    if row[2] == label:
                        return row[0]
                    else: 
                        count+=1
            r_file.close()        
        return None


class Iterator:

    def __init__(self, a: Annotation):
        self.limit = a.number_lines
        self.ann = a
        self.counter = 0

    def __next__(self, label)-> str:
        """Returns the next instance of annotation by label without repetition"""
        if self.counter < self.limit:
            copy = self.ann.next(label)
            self.counter = self.ann.viewed_files
            return copy
        else:
            raise StopIteration


def task1(path: str, ann: Annotation) -> None:
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


def task2(path_main: str, path: str, ann: Annotation) -> None:
    """Copying dataset to another directory (dataset/class_0000.jpg) and creating an annotation"""
    if not os.path.isdir(path):
        os.mkdir(path)
    subfolders = os.listdir(path_main)
    for subfolder in subfolders:
        files=os.listdir(os.path.join(path_main,subfolder))
        for fname in files:
            shutil.copy(os.path.join(path_main,subfolder,fname),path)
            os.rename(os.path.join(path,fname),os.path.join(path, f"{subfolder}_{fname}"))
            ann.add_line(path, f"{subfolder}_{fname}", subfolder)


def task3(path_main: str, path: str, ann: Annotation) -> None:
    """Copying dataset to another directory (dataset/номер.jpg) and creating an annotation"""
    if not os.path.isdir(path):
        os.mkdir(path)
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
    path_main = os.path.join('C:/','Users','user','Desktop','dataset_copy') 
    path1 = 'C:/Users/user/Desktop/dataset1'
    path2 = 'C:/Users/user/Desktop/dataset2'
    A1 = Annotation("task1_csv.csv")
    A2 = Annotation("task2_csv.csv")
    A3 = Annotation("task3_csv.csv")
    task1(path_main, A1)
    task2(path_main,path1,A2)
    task3(path_main,path2,A3)
    iter1 = Iterator(A1)
    iter2 = Iterator(A2)
    iter3 = Iterator(A3)
    print(iter1.__next__("bay horse"))
    print(iter1.__next__("zebra"))
    print(iter1.__next__("zebra"))
    print(iter1.__next__("zebra"))
    print(iter1.__next__("bay horse"))
    
