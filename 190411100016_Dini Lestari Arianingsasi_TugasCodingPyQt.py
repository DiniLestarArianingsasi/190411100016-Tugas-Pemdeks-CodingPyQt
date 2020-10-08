import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#membuat fungsi dengan nama window
def window():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()
   #menyiapkan label dan membuat perulangan dengan for
   textLabel = QLabel(window)
   label = [None]*10
   jumlah = 10
   for nilai in range(10):
       jumlah = jumlah+25
       label [nilai]=QLabel(window)
       label [nilai].setText("Selamat Datang Di Pemrograman Dekstop")
       label [nilai].move(250,jumlah)
   #menentukan ukuran window,titel dan menampilkan
   window.setGeometry(60,60,800,350)
   window.setWindowTitle("Loop")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
