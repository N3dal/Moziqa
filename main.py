#!/usr/bin/python3
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


class TittleBar(QFrame):
    """
        Custom TitleBar;
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainWindow(QMainWindow):
    """"""

    WIDTH = 380
    HEIGHT = 600
    TITLE = "Moziqa"

    OPACITY = 0.94

    STYLESHEET = """
        
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setWindowTitle(MainWindow.TITLE)
        self.setWindowOpacity(MainWindow.OPACITY)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # to make the main window transparent;
        # self.setAttribute(Qt.WA_TranslucentBackground)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
