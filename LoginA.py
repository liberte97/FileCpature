from selenium import webdriver
import time, os, errno, shutil
import pandas as pd
import webbrowser, subprocess, pyautogui
from PIL import ImageGrab

def Login(wd, url):
	wd.get(url)
	LoginXpath = '//*[@id="arGnb"]/div/div/div[3]/div/a[1]'
	wd.find_element_by_xpath(LoginXpath).click()
	time.sleep(2)
	wd.find_element_by_name('userid').send_keys('ID')
	wd.find_element_by_name('password').send_keys('비밀번호')
	time.sleep(1)
	LoginXpath='//*[@id="big_login"]/fieldset/form/a'
	wd.find_element_by_xpath(LoginXpath).click()
	time.sleep(3)

def Main1Page(wd, url):
	wd.get(url)
	TypeXpath = 'XPath 값'
	wd.find_element_by_xpath(TypeXpath).click()
	time.sleep(2)
	wd.find_element_by_name('searchWord').send_keys('입력값')
	time.sleep(2)
	SearchXpath = 'XPath 값'
	wd.find_element_by_xpath(SearchXpath).click()
	time.sleep(5)
    #driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
	
	count = 0
	for i in range(40):
		time.sleep(1)
		im = ImageGrab.grab(bbox=(60, 50, 1250, 1400))
		time.sleep(2)
		im.save(f'.\\Capture1\\Capture{i+1}.png')
		time.sleep(2)
		if (i+1)%20 == 0:
			count = count + 1
			NextXpath = f'XPath 값'
			wd.find_element_by_xpath(NextXpath).click()
			time.sleep(4)

def WebCrawMain(url, title_site):
	wd = webdriver.Chrome('chromedriver.exe')
	wd.implicitly_wait(3)
	wd.set_window_position(50,50)
	wd.set_window_size(1200, 1350)
	Login(wd, url)
	Main1Page(wd, url)

	for i in range(2):
		wd.get(title_site[i+1])
		time.sleep(3)
		im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
		#driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
		im.save(f'.\\Capture2\\Capture{i+1}.png')
		time.sleep(3)
		wd.find_element_by_id(btn_down1).click()
		PointXpath = 'XPath 값'
		wd.find_element_by_xpath(PointXpath).click()
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
	title_site = get_title(".\\testData.xlsx")
	WebCrawMain("URL", title_site)

