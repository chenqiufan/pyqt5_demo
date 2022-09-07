'''名称：风尘音乐播放器
   版本：V0.1
   作者：菌尘
'''
import os
import sys
import time
import random
import configparser
import ffmpeg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class mmwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        self.songs_list=[]

        self.is_playing=False
        self.is_pause=True

        self.layout=QVBoxLayout()

        self.gb1=QGroupBox('正在播放', self)
        self.gb1.setGeometry(200, 50, 400, 60)

        self.gb2=QGroupBox('个人中心', self)
        self.gb2.setGeometry(20, 40, 80, 300)

        self.gb3=QGroupBox('歌曲列表', self)
        self.gb3.setGeometry(200, 180, 300, 130)

        self.h1_layout=QHBoxLayout()
        self.h2_layout=QHBoxLayout()

        self.myfont = QFont('Microsoft YaHei',  20)

        self.my_btn=QPushButton('我的主页', self)
        self.my_btn.setStyle(QStyleFactory.create('Fusion'))
        self.my_btn.setGeometry(30,60,60,20)

        self.fav_btn=QPushButton('收藏页',self)
        self.fav_btn.setStyle(QStyleFactory.create('Fusion'))
        self.fav_btn.setGeometry(30, 100, 60, 20)



        self.lbl_musicname=QLabel('', self)
        self.lbl_musicname.setGeometry(230, 65, 20, 20)
        self.lbl_musicname.adjustSize()

        self.label1 = QLabel('00:00', self)
        self.label1.setStyle(QStyleFactory.create('Fusion'))
        self.label1.setGeometry(170, 60, 20, 20)
        self.label1.adjustSize()

        self.label2 = QLabel('00:00', self)
        self.label2.setStyle(QStyleFactory.create('Fusion'))
        self.label2.setGeometry(605, 60, 20, 20)
        self.label2.adjustSize()

        self.lbl_vol_name=QLabel('音量',self)
        self.lbl_vol_name.setStyle(QStyleFactory.create('Fusion'))
        self.lbl_vol_name.setGeometry(220,120,20,20)
        self.lbl_vol_name.adjustSize()

        self.lbl_volunm=QLabel('0',self)
        self.lbl_volunm.setGeometry(355,125,20,20)
        self.lbl_volunm.adjustSize()

        self.player=QMediaPlayer()
        self.player.setVolume(3)
        self.player.stateChanged.connect(self.do_mediaplayer_statechanged)

        self.posi_fwd_btn=QPushButton('快进', self)
        self.posi_fwd_btn.setStyle(QStyleFactory.create('Fusion'))
        self.posi_fwd_btn.setGeometry(400,120,60,20)
        self.posi_fwd_btn.setIcon(QIcon("C:/Users/rongjv/Desktop/快进.jfif"))
        self.posi_fwd_btn.clicked.connect(self.setsongposi_fwd)

        self.posi_bkd_btn=QPushButton('后退',self)
        self.posi_bkd_btn.setStyle(QStyleFactory.create('Fusion'))
        self.posi_bkd_btn.setGeometry(500,120,60,20)
        self.posi_bkd_btn.setIcon(QIcon("C:/Users/rongjv/Desktop/快退.jfif"))
        self.posi_bkd_btn.clicked.connect(self.setsongposi_bkd)


        self.slider=QSlider(Qt.Horizontal, self)
        self.setStyle(QStyleFactory.create('Fusion'))

        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        #self.slider.valueChanged.connect(self.songposition)
        self.slider.sliderMoved.connect(self.songposition)
        self.slider.sliderPressed.connect(self.sl_pr)
        self.slider.sliderReleased.connect(self.sl_re)
        self.slider.valueChanged.connect(self.sl_vc)

        self.volunm_slider=QSlider(Qt.Horizontal, self)
        self.volunm_slider.setGeometry(250,120,100,20)
        self.volunm_slider.setMinimum(0)
        self.volunm_slider.setMaximum(100)
        self.volunm_slider.valueChanged.connect(self.songvolunm)

        self.open_btn=QPushButton('导入歌曲', self)
        self.open_btn.setStyle(QStyleFactory.create('Fusion'))
        self.open_btn.setGeometry(30, 140, 60, 20)
        self.open_btn.clicked.connect(self.musicfile)

        self.play_btn = QPushButton('', self)
        self.play_btn.setStyle(QStyleFactory.create('Fusion'))
        self.play_btn.setGeometry(520, 85, 20, 25)
        self.play_btn.setIcon(QIcon(QPixmap("playbtn.png")))
        self.play_btn.clicked.connect(self.play_or_stop)

        self.qlist=QListWidget(self)
        self.qlist.doubleClicked.connect(self.doubleplay)
        #self.qlist.setStyle(QStyleFactory.create('Fusion'))
        self.qlist.setGeometry(200, 200, 300, 120)

        self.timer=QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.musictime)

        #测试用
        #self.lbl_text=QLabel(self)
        #self.lbl_text.setGeometry(400,20,100,20)
        #self.lbl_text.setText('000')


        #设置窗口布局
        self.h1_layout.addWidget(self.slider)
        self.gb1.setLayout(self.h1_layout)

        #self.h2_layout.addWidget(self.my_btn)
        #self.h2_layout.addWidget(self.fav_btn)
        #self.gb2.setLayout(self.h2_layout)

        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('风尘播放器')
        self.setWindowIcon(QIcon("E:/10 临时图片/CoDeSys.ico"))
        self.show()

    def do_mediaplayer_statechanged(self,state):
        if state == QMediaPlayer.PlayingState:
            pass
        if state == QMediaPlayer.PausedState:
            pass
        if state == QMediaPlayer.StoppedState:
            self.is_pause = True

    def sl_pr(self):

        self.timer.stop()
        self.cur_posi=self.slider.value()

    def sl_re(self):
        self.player.setPosition(self.slider.value()*1000)
        self.timer.start()
        print(self.player.duration())
    def sl_vc(self):
        ...
        #self.lbl_text.setText(str(self.slider.value()))

    def songvolunm(self):

        self.volumevalue=self.volunm_slider.value()

        self.player.setVolume(self.volumevalue)

        self.lbl_volunm.setText(str(self.volumevalue))
        self.lbl_volunm.adjustSize()

        #print(self.volunm_slider.value())
        #print(self.player.volume())
        #print(self.volumevalue)

    def songposition(self):


        #self.timer.stop()
        self.p1=self.player.duration()
        self.p2=self.p1 / 1000
        self.p3=self.slider.value() * self.p2
        self.ppp = self.slider.value()
        #print(self.p1)
        #print(self.p2)
        #print(self.p3)
        #self.player.setPosition(int(self.p3))
        #self.label1.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))

    def setsongposi_fwd(self):

        self.p=self.player.position()+2000
        self.player.setPosition(self.p)

    def setsongposi_bkd(self):
        self.pp=self.player.position()-2000
        self.player.setPosition(self.pp)

    def musicfile(self):
        #获取歌曲所在文件夹路径
        self.qlist.clear()
        self.cur_path=QFileDialog.getExistingDirectory(self, "选取文件夹", 'D:/')
        #print(self.cur_path)
        #将文件夹中的所有歌曲添加到List中
        for song in os.listdir(self.cur_path):
            self.songs_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
            self.qlist.addItem(song)
            #print(song)

    def musictime(self):

        if self.is_playing:
            self.slider.setMinimum(0)
            self.slider.setMaximum(int(self.player.duration()/1000))

            #self.slider.setValue(self.slider.value() + 1000)

        self.label1.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
        self.label2.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))
        #self.slider.setMaximum(int(self.player.duration()/1000))
        #print(int(self.player.duration()/1000))
        self.cur_posi = int(self.player.position()/1000)
        #self.sliderposi = self.slider.value()
        #print(self.cur_posi)
        self.slider.setValue(self.cur_posi)
        #print(self.cur_posi)

    def choosesongname(self):

        self.index = self.qlist.currentRow()
        self.playsong = self.songs_list[self.index][-1]
        self.playsongname=self.songs_list[self.index][0]
        self.playsong1 = self.playsong.replace('\\', '/')
        #print(self.playsong1)
        self.get_music_info(self.playsong1)
        self.player.setMedia(QMediaContent(QUrl(self.playsong)))

    def doubleplay(self):
        self.is_playing=False
        self.slider.setValue(0)
        self.choosesongname()
        self.is_playing=True
        self.volunm_slider.setValue(3)
        self.play_or_stop()

    def play_or_stop(self):
        if self.qlist.count()==0:
            QMessageBox.about(self,'tips','no music')
            return

        if not self.player.isAudioAvailable():
            self.choosesongname()
            self.lbl_musicname.setText('歌曲名：' + self.playsongname)
            self.lbl_musicname.adjustSize()
            #print(self.slider.maximum())
        if self.is_pause:
            self.player.play()
            #self.play_btn.setText('暂停')
            self.is_pause=False
            self.play_btn.setIcon(QIcon(QPixmap("stopbtn.png")))
        elif  self.is_pause == False:
            self.player.pause()
            #self.play_btn.setText('播放')
            self.is_pause=True

            self.play_btn.setIcon(QIcon(QPixmap("playbtn.png")))

    def get_music_info(self,filename):
        self.fl=filename
        #print(self.fl)
        #self.probe = ffmpeg.probe(self.fl)
        #self.format = self.probe['format']
        #(self.format)


if __name__ =='__main__':

    app=QApplication(sys.argv)
    ex=mmwin()
    sys.exit(app.exec_())




