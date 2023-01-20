from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()

    window.setGeometry(100,100,200,300)
    window.setWindowTitle("Python Oh Yeah")




    layout = QVBoxLayout()

    label = QLabel("Press the Button Below")
    button = QPushButton("Press me!")
    button.clicked.connect(on_clicked)

    layout.addWidget(label)
    layout.addWidget(button)

    window.setLayout(layout)


    window.show()
    app.exec_()
    
def on_clicked():
    print("Hello world")

if __name__ == '__main__':
    main()