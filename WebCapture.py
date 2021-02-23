from selenium import webdriver
import time, os, errno, shutil
import pandas as pd
import webbrowser, subprocess, pyautogui
from PIL import ImageGrab

def WebCrawMain(title_site):
    wd = webdriver.Chrome('chromedriver.exe')
    wd.implicitly_wait(3)
    wd.set_window_position(50,50)
    wd.set_window_size(1100, 1000)
    for i in range(30):
        wd.get(title_site[i+1]) 
        time.sleep(3)
        im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
        im.save(f'.\\Capture2\\Capture{i+1}.png')
    wd.quit()
    
def get_title(path):
    # 엑셀 읽은 다음 전체 길이 및 이름 return
    data = pd.read_excel(path, engine="openpyxl")
    title_site = {}
    title_num  = len(data.index)
    print(data.columns)
    for i in range(title_num):
        title_site[i+1] = data.site[i]
    return title_site

if __name__ == "__main__":
	title_site, title_name = get_title(".\\test.xlsx")
	WebCrawMain(title_site)
