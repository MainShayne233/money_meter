import sys
from PyQt4 import QtGui

def run():
   app = QtGui.QApplication(sys.argv)
   window = QtGui.QWidget()
   label = QtGui.QLabel(window)
   label.setText("Money Meter!!!")
   window.setGeometry(100,100,200,50)
   label.move(50, 20)
   window.setWindowTitle("Money Meter")
   window.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   run()
