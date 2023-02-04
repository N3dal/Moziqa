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
from time import sleep
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

    class Signals(QObject):
        """
            all title bar signals;
        """

        option_btn_clicked = pyqtSignal()
        menu_btn_clicked = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), TitleBar.HEIGHT)

        self.setStyleSheet(TitleBar.STYLESHEET)

        self.old_mouse_position = QPoint()

        self.signals = TitleBar.Signals()

        # create the menu button;
        # to indicate the menu_button is active or not;
        self.menu_btn_status = False
        self.menu_btn = QPushButton(parent=self)
        self.menu_btn.setFixedSize(34, 34)
        self.menu_btn.setIcon(QIcon("./assets/pictures/menu.png"))
        # self.menu_btn.setIconSize(QSize(24, 24))
        self.menu_btn.clicked.connect(self.__menu_btn_event)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.menu_btn.move(0, 0)

        # create the icon;
        self.icon = QPushButton(parent=self)
        self.icon.setIcon(QIcon(defaults.ICON))
        self.icon.setIconSize(QSize(24, 24))
        # self.icon.clicked.connect(self.parent().showMinimized)
        self.icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon.move(135, 5)

        # create the title label;
        self.title_label = QLabel(
            parent=self, text=f"<h3>{defaults.TITLE}</h3>")
        self.title_label.setStyleSheet(TitleBar.LABEL_STYLESHEET)
        self.title_label.move(170, 7)

        # create the close button;
        self.close_btn = QPushButton(parent=self)
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.setIcon(QIcon("./assets/pictures/close.png"))
        self.close_btn.setIconSize(QSize(24, 24))
        self.close_btn.clicked.connect(sys.exit)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.close_btn.move(self.width() - 30, 2)

        # create the minimize button;
        self.minimize_btn = QPushButton(parent=self)
        self.minimize_btn.setFixedSize(30, 30)
        self.minimize_btn.setIcon(QIcon("./assets/pictures/minimize.png"))
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.minimize_btn.clicked.connect(self.parent().showMinimized)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.minimize_btn.move(self.width() - 60, 2)

        # create the more-option button;
        self.more_option_btn = QPushButton(parent=self)
        self.more_option_btn.setFixedSize(30, 30)
        self.more_option_btn.setIcon(QIcon("./assets/pictures/more.png"))
        self.more_option_btn.setIconSize(QSize(24, 24))
        self.more_option_btn.clicked.connect(self.__more_option_btn_event)
        self.more_option_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.more_option_btn.setStyleSheet(TitleBar.BUTTON_STYLESHEET)
        self.more_option_btn.move(self.width() - 90, 2)

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

    def __more_option_btn_event(self):
        """
            event when more option button clicked;

            return None;
        """

        self.signals.option_btn_clicked.emit()

        return None

    def __menu_btn_event(self):
        """
            event when menu button clicked;

            return None;
        """

        if self.menu_btn_status:
            # if the button is active;
            self.menu_btn.setIcon(QIcon("./assets/pictures/menu.png"))
            self.menu_btn_status = False

        else:
            # if the button is not active;
            self.menu_btn.setIcon(QIcon("./assets/pictures/back.png"))
            self.menu_btn_status = True

        self.signals.menu_btn_clicked.emit(self.menu_btn_status)

        return None


class MainFrame(QFrame):
    """
        The main frame that will hold everything;

    """

    STYLESHEET = """

        background-color: #3e3b4e;
        border-top-left-radius: 0px;
        border-top-right-radius:0px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.parent()

        self.setFixedSize(self.parent().width(), self.root.height() - 37)

        self.setStyleSheet(MainFrame.STYLESHEET)

        # create the slide menu as last one,
        # so it will appear on all the widgets;
        self.slide_menu = SlideMenu(parent=self.root)
        self.slide_menu.move(0, TitleBar.HEIGHT)

        label = QLabel(parent=self, text="<h1>Long test text long one</h1>")
        label.move(20, 180)

    def side_menu(self, slide_menu_status: bool):
        """
            show the side menu;
            and blur the content;

            return None;
        """

        if slide_menu_status:
            self.slide_menu.animation_show()

            # create blur effect;
            blur_effect = QGraphicsBlurEffect(blurRadius=3)
            self.setGraphicsEffect(blur_effect)

        else:
            self.slide_menu.animation_hide()
            self.setGraphicsEffect(None)

        return None


class SlideMenu(QFrame):
    """
        slide menu that appear when we click on menu button;
    """

    STYLESHEET = """
        background-color: #7e71a0;
        border-top-left-radius: 0px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    """

    MAX_WIDTH = 210
    MIN_WIDTH = 0

    class Signals(QObject):
        """
            all slide menu signals;
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.parent()

        self.setGeometry(0, 0, 0, self.root.height() - TitleBar.HEIGHT)
        self.setStyleSheet(SlideMenu.STYLESHEET)

        # show animation;
        self.show_animation = QPropertyAnimation(self, b"geometry")
        self.show_animation.setDuration(150)
        self.show_animation.setStartValue(
            QRect(0, TitleBar.HEIGHT, 0, self.height()))
        self.show_animation.setEndValue(
            QRect(0, TitleBar.HEIGHT, SlideMenu.MAX_WIDTH, self.height()))

        # hide animation;
        self.hide_animation = QPropertyAnimation(self, b"geometry")
        self.hide_animation.setDuration(150)
        self.hide_animation.setStartValue(
            QRect(0, TitleBar.HEIGHT, SlideMenu.MAX_WIDTH, self.height()))
        self.hide_animation.setEndValue(
            QRect(0, TitleBar.HEIGHT, 0, self.height()))

    def animation_show(self):
        """
            show the Slide Menu with animation;

            return None;
        """

        self.show_animation.start()

        return None

    def animation_hide(self):
        """
            hide the Slide Menu with animation;

            return None;
        """

        self.hide_animation.start()

        return None


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
        self.setWindowIcon(QIcon(defaults.ICON))
        self.setWindowFlags(Qt.FramelessWindowHint)

        # to make the main window transparent;
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.title_bar = TitleBar(parent=self)
        self.title_bar.move(0, 0)

        self.main_frame = MainFrame(parent=self)
        self.main_frame.move(0, TitleBar.HEIGHT)

        self.title_bar.signals.menu_btn_clicked.connect(
            self.main_frame.side_menu)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
