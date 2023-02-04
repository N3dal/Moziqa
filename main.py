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
import defaults


# wipe terminal screen;
system("clear")


class TitleBar(QFrame):
    """
           Custom Title bar for the Main window;
    """

    HEIGHT = 34

    STYLESHEET = """
        background-color: #8b949e;

        border-top-left-radius: 10px;
        border-top-right-radius:10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;

    """

    LABEL_STYLESHEET = """
        color: black;
        font-weight: bold;
        font-family: Mono;
    """

    BUTTON_STYLESHEET = """
        QPushButton{
            border-radius: 5px;
        }
        
        QPushButton:hover{
            background-color: #d8e1ee;
        }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), TitleBar.HEIGHT)

        self.setStyleSheet(TitleBar.STYLESHEET)

        self.old_mouse_position = QPoint()

        # create the menu button;
        self.menu_btn = QPushButton(parent=self)
        self.menu_btn.setFixedSize(34, 34)
        self.menu_btn.setIcon(QIcon("./assets/pictures/menu.png"))
        self.menu_btn.setIconSize(QSize(24, 24))
        # self.menu_btn.clicked.connect(self.parent().showMinimized)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.menu_btn.move(0, 0)

        # create the icon;
        self.icon = QPushButton(parent=self)
        self.icon.setIcon(QIcon("./assets/pictures/icon.png"))
        self.icon.setIconSize(QSize(24, 24))
        # self.icon.clicked.connect(self.parent().showMinimized)
        self.icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon.move(45, 3)

        # create the title label;
        self.title_label = QLabel(
            parent=self, text=f"<h3>{defaults.TITLE}</h3>")
        self.title_label.setStyleSheet(TitleBar.LABEL_STYLESHEET)
        self.title_label.move(80, 7)

        # create the close button;
        self.close_btn = QPushButton(parent=self)
        self.close_btn.setIcon(QIcon("./assets/pictures/close.png"))
        self.close_btn.setIconSize(QSize(24, 24))
        self.close_btn.clicked.connect(sys.exit)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.close_btn.move(self.width() - 30, 5)

        # create the minimize button;
        self.minimize_btn = QPushButton(parent=self)
        self.minimize_btn.setIcon(QIcon("./assets/pictures/minimize.png"))
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.minimize_btn.clicked.connect(self.parent().showMinimized)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.minimize_btn.move(self.width() - 60, 5)

        # create the more-option button;
        self.more_option_btn = QPushButton(parent=self)
        self.more_option_btn.setIcon(QIcon("./assets/pictures/options.png"))
        self.more_option_btn.setIconSize(QSize(24, 24))
        # self.more_option_btn.clicked.connect(self.parent().showMinimized)
        self.more_option_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.more_option_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.more_option_btn.move(self.width() - 90, 5)

    def mousePressEvent(self, e):

        self.old_mouse_position = e.globalPos()

        self.setCursor(QCursor(Qt.DragMoveCursor))

        return None

    def mouseReleaseEvent(self, e):

        self.setCursor(QCursor(Qt.ArrowCursor))

        return None

    def mouseMoveEvent(self, e):

        delta = QPoint(e.globalPos() - self.old_mouse_position)

        self.parent().move(self.parent().x() + delta.x(), self.parent().y() + delta.y())
        self.old_mouse_position = e.globalPos()

        return None


class MainFrame(QFrame):
    """
        The main frame that will hold everything;

    """

    STYLESHEET = """
        
        background-color: #282828;
        border-top-left-radius: 0px;
        border-top-right-radius:0px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
        
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), self.parent().height() - 37)

        self.setStyleSheet(MainFrame.STYLESHEET)


class MainWindow(QMainWindow):
    """"""

    WIDTH = 380
    HEIGHT = 600

    OPACITY = 1.0

    STYLESHEET = """
        
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setWindowOpacity(MainWindow.OPACITY)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # to make the main window transparent;
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.title_bar = TitleBar(parent=self)
        self.title_bar.move(0, 0)

        self.main_frame = MainFrame(parent=self)
        self.main_frame.move(0, TitleBar.HEIGHT)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
