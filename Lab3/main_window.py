from annotation_iterator import AnnotationIterator as AnnIt
from annotation import Annotation 
from copy_and_ann__2 import copy_and_annotation as copy_and_ann
from copy_random__3 import random_copy 
from creat_ann__1 import creat_annotation 
import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QMainWindow, QFileDialog, 
        QLabel, QGridLayout)
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Work with dataset")

        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select folder source dataset')
        src = QLabel(f'Исходный датасет:\n{self.folder_path}', self)
        layout = QGridLayout()
        layout.addWidget(src, 0, 0)

        create_annotation_button = QPushButton("Сформировать аннотацию")
        create_annotation_button.setFixedSize(QSize(250, 50))
        create_annotation_button.clicked.connect(self.create_annotation)
        layout.addWidget(create_annotation_button, 1, 0)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def create_annotation(self) -> None:
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter file name:')
        if ok:
            print(str(text))
            A = Annotation( f"{str(text)}.cvs")
            creat_annotation(self.folder_path, A)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()