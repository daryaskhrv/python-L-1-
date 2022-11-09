from annotation_iterator import AnnotationIterator as AnnIt
from annotation import Annotation 
from copy_and_ann__2 import copy_and_annotation as copy_and_ann
from copy_random__3 import random_copy 
from creat_ann__1 import creat_annotation 
import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QMainWindow, QFileDialog, 
        QLabel, QGridLayout,QVBoxLayout, QSizePolicy)
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtGui

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(700,400)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Work with dataset")
        self.center()
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Выберите папку исходного датасета')

        src = QLabel(f'Исходный датасет:\n{self.folder_path}', self)
        src.setFixedSize(QSize(250, 50))
        src.move(5,0)
        
        button_create_annotation = self.add_button("Сформировать аннотацию", 250, 50, 5, 50)
        button_create_annotation.clicked.connect(self.create_annotation)

        button_copy_dataset = self.add_button("Скопировать датасет", 250, 50, 5, 100)
        button_copy_dataset.clicked.connect(self.dataset_copy)

        button_copy_random_dataset = self.add_button("Рандом датасета", 250, 50, 5, 150)
        button_copy_random_dataset.clicked.connect(self.dataset_random)


        next_tiger_button = self.add_button("Следующий тигр", 250, 50, 5, 200)
        #self.next_tiger_button.clicked.connect(self.next_tiger)

        next_leopard_button = self.add_button("Следующий леопард", 250, 50, 5, 250)
        #self.next_leopard_button.clicked.connect(self.next_leopard)

        self.label_image = QLabel('Нажмите кнопку "Следующий тигр" или "Следующий леопард".')
        self.label_image.setMinimumSize(QSize(500, 300))
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.show()

    def add_button(self, name: str, size_x: int, size_y: int, pos_x: int, pos_y: int):
        """Add button with a fixed size and position"""
        button = QPushButton(name, self)
        button.setFixedSize(QSize(size_x, size_y))
        button.move(pos_x, pos_y)
        return button

    def center(self):
        """Window centering"""
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create_annotation(self) -> None:
        """Creat annotation of the dataset with chosen name"""
        text, ok = QInputDialog.getText(self, 'Ввод',
            'Введите название файла-аннотации:')
        if ok:
            A = Annotation( f"{str(text)}.cvs")
            creat_annotation(self.folder_path, A)

    def dataset_copy(self)-> None:
        """Copying dataset (dataset/class_0000.jpg) and creating an annotation"""
        path_copy = QFileDialog.getExistingDirectory(self, 'Введите путь к папке, в которую будет скопирован датасет')
        text, ok = QInputDialog.getText(self, 'Ввод',
            'Введите название файла-аннотации:')
        if ok:
            A = Annotation( f"{str(text)}.cvs")
            copy_and_ann(self.folder_path, path_copy, A)

    def dataset_random(self)-> None:
        """Copying dataset (dataset/номер.jpg) and creating an annotation"""
        path_copy = QFileDialog.getExistingDirectory(self, 'Введите путь к папке, в которую будет скопирован датасет')
        text, ok = QInputDialog.getText(self, 'Ввод',
            'Введите название файла-аннотации:')
        if ok:
            A = Annotation( f"{str(text)}.cvs")
            random_copy(self.folder_path, path_copy, A)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()