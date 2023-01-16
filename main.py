# -----------------------------------------------------------------
# This is one of the 50 python projects
# GUI music player, simple one only start and pause the song.
#
#
# Author:N84.
#
# Create Date:Mon Apr 26 05:45:49 2021.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import (system, listdir)
from os.path import exists
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import vlc


# wipe terminal screen;
system("clear")


class MainWindow(QMainWindow):
    """"""
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        


def main():

    app = QApplication(sys.argv)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
