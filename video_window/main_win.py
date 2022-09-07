# coding=utf-8
import os

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QPushButton, QGroupBox, QStyleFactory, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer

import time


class AudioPlayer(QWidget):

    def __init__(self):
        super(AudioPlayer, self).__init__()

        self.is_playing = False

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("电话会议")
        self.setFixedSize(800, 500)
        self.setWindowIcon(QIcon("./images/2.jpeg"))
        self.center()

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(800, 430)
        image_pix = QPixmap("./images/4.png")
        self.image_label.setPixmap(image_pix)

        # play_button = QPushButton("play", self)
        # play_button.setStyleSheet("QPushButton{border-image: url(./images/play.jpeg)}")
        # play_button.setFixedSize(50, 50)
        # play_button.move(375, 450)
        self.admin_group = QGroupBox("正在播放", self)
        self.admin_group.setGeometry(200, 430, 400, 50)

        self.left_time_label = QLabel("00:00", self)
        self.left_time_label.setStyle(QStyleFactory.create("Fusion"))
        self.left_time_label.setGeometry(170, 420, 50, 50)

        self.right_time_label = QLabel("00:00", self)
        self.right_time_label.setStyle(QStyleFactory.create("Fusion"))
        self.right_time_label.setGeometry(600, 420, 50, 50)

        self.audio_player = QMediaPlayer()
        self.audio_player.setVolume(3)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setStyle(QStyleFactory.create("Fusion"))
        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        self.slider.setGeometry(200, 450, 400, 20)
        self.slider.sliderMoved.connect(self.song_position)

        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.music_time)

        # self.volume_slider = QSlider(Qt.Horizontal, self)
        # self.volume_slider.setGeometry(200, 450, 400, 20)
        # self.volume_slider.setMinimum(0)
        # self.volume_slider.setMaximum(1000)

        test_button = QPushButton("选择音乐", self)
        test_button.setGeometry(10, 450, 100, 40)
        test_button.clicked.connect(self.play_music)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)

    def play_music(self):
        self.slider.setValue(0)
        file_path = os.path.abspath(__file__)
        dir_path = os.path.dirname(file_path)
        song_path = os.path.join(dir_path + r"\audios\song.mp3")
        print(song_path)
        self.audio_player.setMedia(QMediaContent(QUrl.fromLocalFile(song_path)))
        self.audio_player.play()
        self.timer.start()

    def music_time(self):
        if self.is_playing:
            self.slider.setMinimum(0)
            self.slider.setMaximum(int(self.audio_player.duration() / 1000))

        self.left_time_label.setText(time.strftime('%M:%S', time.localtime(self.audio_player.position() / 1000)))
        self.right_time_label.setText(time.strftime('%M:%S', time.localtime(self.audio_player.duration() / 1000)))

        cur_posi = int(self.audio_player.position() / 1000)
        self.slider.setValue(cur_posi)

    def sl_re(self):
        self.audio_player.setPosition(self.slider.value() * 1000)

    def music_file(self):
        cur_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        print(cur_path)
        for song in os.listdir(cur_path):
            print(os.path.join(cur_path, song))

    def song_position(self):
        p1 = self.audio_player.duration()
        p2 = p1 / 1000
        p3 = self.slider.value() * p2
        p4 = self.slider.value()
        self.audio_player.setPosition(int(p3))
        self.left_time_label.setText(time.strftime('%M:%S', time.localtime(self.audio_player.position() / 1000)))


