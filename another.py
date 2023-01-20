from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()

    window.setGeometry(100,100,200,300)
    window.setWindowTitle("Python Oh Yeah")





    window.show()
    app.exec_()
    
def on_clicked():
    print("Hello world")

if __name__ == '__main__':
    main()