import csv
import os


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
        return None