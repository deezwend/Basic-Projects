#<frameworks>
from pytube import YouTube
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter.messagebox import showerror as hata, showinfo as bilgi, showwarning as uyari, askyesno as soru
from sys import argv, exit as exiting
from threading import Thread as th
from GUI import *
from numpy import arange as range
import sqlite3 as sql
import youtube_dl
import vlc
import time
import os
#</frameworks>
#<podcast_video_player>
class Podcast_Video_Player(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PodcastVideoPlayer()
        self.ui.setupUi(self)
        self.isvideoplaying = False
        self.arevideosdownloading = False
        self.show()
        self.database = sql.connect("videos.db", check_same_thread=False)
        self.database.execute("""CREATE TABLE IF NOT EXISTS videos (
            videoid INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            videotitle TEXT NOT NULL,
            videolink TEXT NOT NULL
            )""")
        self.crs = self.database.cursor()
        self.AddListVideos()
        if self.countofvideos < 1:
            self.ui.tabWidget.setTabVisible(1, False)
            uyari(message="The tab of 'See saved videos' has been hidden because of no videos exist in database.")
        self.ui.btnSave.clicked.connect(self.SaveVideo)
        self.ui.btnDeleteVideo.clicked.connect(self.DeleteVideo)
        self.ui.btnPlayVideo.clicked.connect(self.PlayVideo)
        self.ui.btnDownloadVideo.clicked.connect(self.DownloadVideo)
    
    def AddListVideos(self):
        self.ui.lstSavedVideos.clear()
        self.countofvideos = len(self.crs.execute("SELECT * FROM videos").fetchall())
        if self.countofvideos > 0:
            if self.ui.tabWidget.isTabVisible(0):
                self.ui.tabWidget.setTabVisible(1, True)
        self.crs.execute("SELECT videotitle FROM videos")
        for i in self.crs:
            self.ui.lstSavedVideos.addItem(str(i[0]).replace("'","").replace('"',""))
        
        
    def SaveVideo(self):
        link = self.ui.lneVideoLink.text().replace("www.","")
        if link == "" or not link[0:28] == "https://youtube.com/watch?v=":
            self.ui.lneVideoLink.setText("")
            hata(message="Please enter a video link here.")
            return None
        else:
            forcheck = self.crs.execute("SELECT videotitle FROM videos")
            yt = YouTube(link)
            title = yt.title.replace("'","").replace('"',"")
            self.ui.lneVideoLink.setText("")
            for i in forcheck.fetchall():
                if title in i[0]:
                    print("x")
            self.crs.execute("INSERT INTO videos (videotitle, videolink) VALUES (?,?)",(title, link))
            self.database.commit()
            bilgi(message="The video has been saved.")  
            self.AddListVideos()
            del forcheck, yt, title
    
    def DeleteVideo(self):
        if bool(self.ui.lstSavedVideos.currentItem()) is False:
            hata(message="You did not select any video from the list.")
            return
        else:
            try:
                self.crs.execute(fr"DELETE FROM videos WHERE videotitle='{self.ui.lstSavedVideos.currentItem().text()}'")
                self.AddListVideos()
                self.database.commit()
                bilgi(message="The video has been deleted.")
            except:
                hata(message="An unknown error.")
                return
    
       
    def PlayVideo(self):
        def PlayVideo_thread():
            if (not bool(self.ui.lstSavedVideos.currentItem())):
                hata(message="You did not select any video from the list.")
                return
            if not self.ui.chkPlayAllOfVideos.isChecked():
                if self.isvideoplaying == False:
                    self.isvideoplaying = True
                    videolink = self.crs.execute(rf"SELECT videolink FROM videos WHERE videotitle='{self.ui.lstSavedVideos.currentItem().text()}'").fetchone()[0]
                    yt = YouTube(videolink)
                    self.ui.lblPlayingVideo.setVisible(True)
                    self.ui.lblAuthorName.setVisible(True)
                    self.ui.lblVideoName.setText(yt.title)
                    self.ui.lblChannelName.setText(yt.author)
                    videolink = videolink.split("watch?v=")[1]
                    yt = yt.length + 1
                    youtube_dl_options = {'quiet': True, 'format': 'bestaudio'} 
                    with youtube_dl.YoutubeDL() as yt_dl:
                        info = yt_dl.extract_info(f"{videolink}", download=False)
                        audio_url = info['formats'][0]['url']
                        player = vlc.MediaPlayer(audio_url)
                        player.play()
                        time.sleep(yt)
                        self.isvideoplaying = False
                        self.ui.lblPlayingVideo.setVisible(False)
                        self.ui.lblAuthorName.setVisible(False)
                        self.ui.lblChannelName.setText("")
                        self.ui.lblVideoName.setText("")
                else:
                    hata(message="An another audio is already being played.")
                    return None
            else:
                if self.isvideoplaying == False:
                    self.isvideoplaying = True
                    for i in range(self.ui.lstSavedVideos.count()):
                        videolink = self.crs.execute(rf"SELECT videolink FROM videos WHERE videotitle='{self.ui.lstSavedVideos.item(i).text()}'").fetchone()[0]
                        yt = YouTube(videolink)
                        self.ui.lblPlayingVideo.setVisible(True)
                        self.ui.lblAuthorName.setVisible(True)
                        self.ui.lblVideoName.setText(yt.title)
                        self.ui.lblChannelName.setText(yt.author)
                        videolink = videolink.split("watch?v=")[1]
                        yt = yt.length + 1
                        youtube_dl_options = {'quiet': True, 'format': 'bestaudio'} 
                        with youtube_dl.YoutubeDL() as yt_dl:
                            info = yt_dl.extract_info(f"{videolink}", download=False)
                            audio_url = info['formats'][0]['url']
                            player = vlc.MediaPlayer(audio_url)
                            player.play()
                            time.sleep(yt)
                            self.isvideoplaying = False
                    self.ui.lblPlayingVideo.setVisible(False)
                    self.ui.lblAuthorName.setVisible(False)
                    self.ui.lblVideoName.setText("")
                    self.ui.lblChannelName.setText("")
                    del videolink, yt, info, audio_url, player, youtube_dl_options
                else:
                    hata(message="An another audio is already being played.")
                    return None
        
        t1 = th(target=PlayVideo_thread)
        t1.start()
        
    def DownloadVideo(self):
        def DownloadVideo_thread():
            if (not bool(self.ui.lstSavedVideos.currentItem())):
                hata(message="You did not select any video from the list.")
                return
            
            if not self.arevideosdownloading:
                self.arevideosdownloading = True
                if self.ui.chkDownloadAllOfVideos.isChecked():
                    for i in range(self.ui.lstSavedVideos.count()):
                        video = self.crs.execute(rf"SELECT videolink FROM videos WHERE videotitle='{self.ui.lstSavedVideos.item(i).text()}'").fetchone()[0]
                        yt = YouTube(video)
                        if self.ui.chkSetQuality.isChecked():
                            download = yt.streams.get_by_resolution(self.ui.cmbQualities.currentText())
                        else:
                            download = yt.streams.get_highest_resolution()
                        download.download(os.getcwd())
                    self.arevideosdownloading = False
                    bilgi(message="All videos downloaded.")
                    del video, yt, download
                else:
                    video = self.crs.execute(rf"SELECT videolink FROM videos WHERE videotitle='{self.ui.lstSavedVideos.currentItem().text()}'").fetchone()[0]
                    yt = YouTube(video)
                    if self.ui.chkSetQuality.isChecked():
                        download = yt.streams.get_by_resolution(self.ui.cmbQualities.currentText())
                    else:
                        download = yt.streams.get_highest_resolution()
                    download.download(os.getcwd())
                    bilgi(message="The video downloaded.")
                    del yt, download, video
                    return
                    
                        
            else:
                hata(message="An another video is already being downloaded.")
        t1 = th(target=DownloadVideo_thread)
        t1.start()  
        
#</podcast_video_player>



if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = Podcast_Video_Player()
    exiting(app.exec_())

"""
<TODO>
1) Önce program için bir arayüz yapacağım.//
2) Arayüzün CSS'ini ayarlayacağım.//
3) Arayüzdeki bağlantıları, fonksiyonları ayarlayacağım.//
4) Sırasıyla bütün videoları oynatma özelliği ekleyeceğim.//
5) Video oynatımı bittikten sonra oynatılan videoyu listeden silme özelliği ekleyeceğim.--
6) İstediğim videoları bir veritabanına kaydedeceğim.//
7) İstediğim zaman listeden bir video silebileceğim.//
8) İstersem videoyu programın bulunduğu konuma indirme özelliği ekleyeceğim.--
</TODO>
"""

