#!/usr/bin/env python
# -*- encoding: utf8 -*-
import sys
import titi_app

def main():
    app = titi_app.QtGui.QApplication(sys.argv)
    ventana = titi_app.MainApp()
    width = 973
    height = 653
    ventana.setFixedSize(width, height)
    ventana.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()

