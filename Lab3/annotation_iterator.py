from annotation import Annotation
from creat_ann__1 import creat_annotation as cr_ann

class AnnotationIterator:

    def __init__(self, a: Annotation):
        self.ann = a
        self.counter = 0

    def __next__(self, label)-> str:
        """Returns the next instance of annotation by label without repetition"""
        if self.counter < (self.ann.number_lines-1):
            copy = self.ann.next(label)
            self.counter = self.ann.viewed_files
            return copy
        else:
            raise StopIteration


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    A = Annotation("task1_csv.csv")
    cr_ann(path_main, A)
    iter = AnnotationIterator(A)
    print(iter.__next__("bay horse"))
    print(iter.__next__("zebra"))
    print(iter.__next__("zebra"))
    print(iter.__next__("zebra"))
    print(iter.__next__("bay horse"))            