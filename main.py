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


class Gif(QLabel):
    """
        custom label that only show gifs;
    """

    class Signals(QObject):
        """
            all Gif signals;
        """

        clicked = pyqtSignal()

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = path

        self.signals = Gif.Signals()

        self.animation_status = False

        self.setAlignment(Qt.AlignCenter)
        self.__gif = QMovie(self.path)

        self.setMovie(self.__gif)

    def start(self):
        """
            start the animation;

            return None;
        """

        self.__gif.start()
        self.animation_status = True

        return None

    def stop(self):
        """
            stop the animation;

            return None;
        """

        self.__gif.stop()
        self.animation_status = False

        return None

    def show_picture(self):
        """
            show the first frame from the movie;

            return None;
        """

        self.start()
        self.stop()

        return None

    def mousePressEvent(self, e):
        """
            press event on the label;

            return None;
        """

        if e.type() == 4:
            # double click;
            self.signals.clicked.emit()

        return None


class MusicControl(QFrame):
    """"""

    WIDTH = 330
    HEIGHT = 60

    STYLESHEET = """
            background-color: #535066;
            border-radius: 10px;
        
    """

    BUTTON_STYLESHEET = """
        QPushButton{
            border-radius: 16px;
        }
        
        QPushButton:hover{
            background-color: #3e3b4e;
            
        }        
    """

    class Signals(QObject):
        """
            all signals for music control;
        """

        previous_clicked = pyqtSignal()
        play_control_clicked = pyqtSignal(bool)
        next_clicked = pyqtSignal()
        repeat_clicked = pyqtSignal(bool)
        sound_clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MusicControl.WIDTH, MusicControl.HEIGHT)
        self.setStyleSheet(MusicControl.STYLESHEET)

        self.signals = MusicControl.Signals()

        self.__play_state = False
        self.__repeat_state = False

        self.play_btn = QPushButton(parent=self)
        self.play_btn.setFixedSize(32, 32)
        self.play_btn.setStyleSheet(MusicControl.BUTTON_STYLESHEET)
        self.play_btn.clicked.connect(self.__play_btn_event)
        self.play_btn.setIcon(QIcon("./assets/pictures/play.png"))
        self.play_btn.setIconSize(QSize(32, 32))
        self.play_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_btn.move(
            (self.width() - self.play_btn.width()) // 2, (self.height() - self.play_btn.height()) // 2)

        self.previous_btn = QPushButton(parent=self)
        self.previous_btn.setFixedSize(32, 32)
        self.previous_btn.setStyleSheet(MusicControl.BUTTON_STYLESHEET)
        self.previous_btn.setIcon(QIcon("./assets/pictures/previous.png"))
        self.previous_btn.setIconSize(QSize(32, 32))
        self.previous_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_btn.move(
            self.play_btn.x() - 70, (self.height() - self.previous_btn.height()) // 2)

        self.next_btn = QPushButton(parent=self)
        self.next_btn.setFixedSize(32, 32)
        self.next_btn.setStyleSheet(MusicControl.BUTTON_STYLESHEET)
        self.next_btn.setIcon(QIcon("./assets/pictures/next.png"))
        self.next_btn.setIconSize(QSize(32, 32))
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_btn.move(
            self.play_btn.x() + 70, (self.height() - self.next_btn.height()) // 2)

        self.repeat_btn = QPushButton(parent=self)
        self.repeat_btn.setFixedSize(32, 32)
        self.repeat_btn.setStyleSheet(MusicControl.BUTTON_STYLESHEET)
        self.repeat_btn.clicked.connect(self.__repeat_btn_event)
        self.repeat_btn.setIcon(QIcon("./assets/pictures/repeat_diactive.png"))
        self.repeat_btn.setIconSize(QSize(32, 32))
        self.repeat_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.repeat_btn.move(self.play_btn.x() - 120,
                             (self.height() - self.repeat_btn.height()) // 2)

        self.volume_btn = QPushButton(parent=self)
        self.volume_btn.setFixedSize(32, 32)
        self.volume_btn.setStyleSheet(MusicControl.BUTTON_STYLESHEET)
        self.volume_btn.setIcon(QIcon("./assets/pictures/volume.png"))
        self.volume_btn.setIconSize(QSize(32, 32))
        self.volume_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.volume_btn.move(self.play_btn.x() + 120,
                             (self.height() - self.volume_btn.height()) // 2)

    @property
    def play_state(self):
        return self.__play_state

    @property
    def repeat_state(self):
        return self.__repeat_state

    def __repeat_btn_event(self):
        """
            event when we click on repeat button;

            return None;
        """

        if self.repeat_state:
            self.repeat_btn.setIcon(
                QIcon("./assets/pictures/repeat_diactive.png"))
            self.__repeat_state = False

        else:
            self.repeat_btn.setIcon(
                QIcon("./assets/pictures/repeat_active.png"))
            self.__repeat_state = True

        self.signals.repeat_clicked.emit(self.repeat_state)

        return None

    def __play_btn_event(self):
        """
            event when we click on play button;

            return None;
        """

        if self.play_state:
            self.play_btn.setIcon(QIcon("./assets/pictures/play.png"))
            self.__play_state = False

        else:
            self.play_btn.setIcon(QIcon("./assets/pictures/pause.png"))
            self.__play_state = True

        self.signals.play_control_clicked.emit(self.play_state)

        return None

    def __previous_btn_event(self):
        """"""

    def __next_btn_event(self):
        """"""

    def __volume_btn_event(self):
        """"""


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
        icon_clicked = pyqtSignal()

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
        self.icon.clicked.connect(self.__icon_btn_event)
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

    def __icon_btn_event(self):
        """
            event when we click on the icon;

            return None;
        """

        self.signals.icon_clicked.emit()

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

    ALBUM_LOGO_STYLESHEET = """
        background-color: #535066;
        border-radius: 10px;
    """

    SONG_LABEL_STYLESHEET = """
        border-radius: 10px;
        font-size: 22px;
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.parent()

        self.setFixedSize(self.root.width(), self.root.height() - 37)

        self.setStyleSheet(MainFrame.STYLESHEET)

        # create the slide menu as last one,
        # so it will appear on all the widgets;
        self.slide_menu = SlideMenu(parent=self.root)
        self.slide_menu.move(0, TitleBar.HEIGHT)

        # create the default album logo;
        self.album_logo = Gif(
            parent=self, path="./assets/gifs/music_anim2.gif")
        self.album_logo.setFixedSize(320, 250)
        self.album_logo.setStyleSheet(MainFrame.ALBUM_LOGO_STYLESHEET)
        self.album_logo.show_picture()
        self.album_logo.move((self.width() - self.album_logo.width()) // 2, 50)

        # create the song name label;
        self.song_name_label = QLabel(
            parent=self, text="Long Text Just For testing!")
        self.song_name_label.setFixedSize(self.width(), 40)
        self.song_name_label.setStyleSheet(MainFrame.SONG_LABEL_STYLESHEET)
        self.song_name_label.setAlignment(Qt.AlignCenter)
        self.song_name_label.move(0, 330)

        # create the music control;
        self.music_control = MusicControl(parent=self)
        self.music_control.signals.play_control_clicked.connect(
            self.album_logo_animation)
        self.music_control.move(
            (self.width() - self.music_control.width()) // 2, 390)

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

            # remove the blur effect;
            self.setGraphicsEffect(None)

        return None

    def album_logo_animation(self, btn_state: bool):
        """
            click event when click on the album logo;

            return None;
        """

        if self.album_logo.animation_status or not btn_state:
            self.album_logo.stop()

        else:
            self.album_logo.start()

        return None


class SlideMenu(QFrame):
    """
        slide menu that appear when we click on menu button;
    """

    STYLESHEET = """
        background-color: #6c6785;
        border-top-left-radius: 0px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    """

    MAX_WIDTH = 210
    MIN_WIDTH = 0
    ANIMATION_DURATION = 150

    class Signals(QObject):
        """
            all slide menu signals;
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.parent()

        self.setGeometry(0, TitleBar.HEIGHT, 0,
                         self.root.height() - TitleBar.HEIGHT - 3)
        self.setStyleSheet(SlideMenu.STYLESHEET)

        # show animation;
        self.show_animation = QPropertyAnimation(self, b"geometry")
        self.show_animation.setDuration(SlideMenu.ANIMATION_DURATION)
        self.show_animation.setStartValue(
            QRect(0, TitleBar.HEIGHT, 0, self.height()))
        self.show_animation.setEndValue(
            QRect(0, TitleBar.HEIGHT, SlideMenu.MAX_WIDTH, self.height()))

        # hide animation;
        self.hide_animation = QPropertyAnimation(self, b"geometry")
        self.hide_animation.setDuration(SlideMenu.ANIMATION_DURATION)
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
        self.main_frame.move(0, TitleBar.HEIGHT - 1)

        self.title_bar.signals.menu_btn_clicked.connect(
            self.main_frame.side_menu)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
